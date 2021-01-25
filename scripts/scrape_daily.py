import urllib.request
import json
import datetime
from dateutil.parser import parse
from general_utils import log_error, file_len
import pathlib
import sqlite3
import pytz
current_directory = str(pathlib.Path(__file__).parent.absolute())


def get_daily_id(target_date=False):
    if target_date == False:
        target_date = datetime.date.today()
        print("No target_date supplied, defaulting to today.")

    url = f'https://api.pushshift.io/reddit/search/submission/?subreddit=wallstreetbets&title=Daily%20Discussion%20Thread%20for%20{target_date.strftime("%B")}%20{str(int(target_date.strftime("%d")))}%2C%20{target_date.strftime("%Y")}'

    json_response = json.loads(urllib.request.urlopen(url).read().decode())

    for post in json_response["data"]:
        if post['title'].startswith('Daily Discussion Thread'):
            date = " ".join(post['title'].split(' ')[-3:])
            parsed = parse(date) 
            if parse(str(target_date)) == parsed:
                submission_id = post['id']
    
    try:
        print(f"Daily discussion id: {submission_id}")
        return(submission_id)
    except:
        msg = f"Daily discussion thread for {target_date} not found. Is the market open on this date? Search url used: {url}"
        log_error(msg+"\n")
        raise Exception(msg)


def get_comment_ids(submission_id):
    url = f"https://api.pushshift.io/reddit/submission/comment_ids/{submission_id}"
    return json.loads(urllib.request.urlopen(url).read().decode())['data']

def pull_comments(comment_ids):
    conn = sqlite3.connect(f"{current_directory}/../tickerdat.db")
    c = conn.cursor()
    for i in range(int(len(comment_ids)/1000)):
        print(f"{i*1000} / {len(comment_ids)}")

        comment_ids_group = comment_ids[i*1000:(i+1)*1000]
        url = f"https://api.pushshift.io/reddit/comment/search?ids={','.join(comment_ids_group)}&fields=body,all_awardings,author,created_utc,permalink"

        while True:
            try:
                new_comments = json.loads(urllib.request.urlopen(url).read().decode())['data']
                test = new_comments[0]['created_utc']
                break
            except:
                print("Pushshift API call failed, trying again in 10 seconds...")


        for comment in new_comments:
            text = comment['body']
            text = text.replace("\n"," ")
            date_created = str(datetime.datetime.fromtimestamp(comment["created_utc"]).astimezone(pytz.timezone('US/Eastern')).date())
            if len(comment['all_awardings']) == 0:
                awards = 0
            else:
                awards = str(comment['all_awardings'])
            c.execute(f"INSERT INTO daily_discussion_comment_data VALUES (?,?,?,?,?)", (awards, comment['author'], text, date_created, comment["created_utc"]))
        conn.commit()
        conn.close()
    
    comment_ids_group = comment_ids[int(len(comment_ids)/1000)*1000:]
    url = f"https://api.pushshift.io/reddit/comment/search?ids={','.join(comment_ids_group)}&fields=body,all_awardings,author,created_utc"
    while True:
        try:
            new_comments = json.loads(urllib.request.urlopen(url).read().decode())['data']
            test = new_comments[0]['created_utc']
            break
        except:
            print("Pushshift API call failed, trying again in 10 seconds...")


    for comment in new_comments:
        text = comment['body']
        text = text.replace("\n"," ")
        date_created = str(datetime.datetime.fromtimestamp(comment["created_utc"]).astimezone(pytz.timezone('US/Eastern')).date())
        if len(comment['all_awardings']) == 0:
            awards = 0
        else:
            awards = str(comment['all_awardings'])
        c.execute(f"INSERT INTO daily_discussion_comment_data VALUES (?,?,?,?,?)", (awards, comment['author'], text, date_created, comment["created_utc"]))
    conn.commit()
    conn.close()


        



if __name__ == "__main__":
    target_date = datetime.date(int(input("Year: ")), int(input("Month: ")), int(input("Day: "))) # datetime.datetime(2021, 1, 21) # 
    get_daily_id(target_date=target_date)
    comment_ids = get_comment_ids("kjdkdk")
    pull_comments(comment_ids)



# TODO: search top posts of the day and their comments