import urllib.request
import json
import datetime
from dateutil.parser import parse
from general_utils import log_error, file_len


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
    all_comments = []
    for i in range(int(len(comment_ids)/1000)):
        print(f"{i*1000} / {len(comment_ids)}")

        comment_ids_group = comment_ids[i*1000:(i+1)*1000]
        url = f"https://api.pushshift.io/reddit/comment/search?ids={','.join(comment_ids_group)}"

        while True:
            try:
                new_comments = json.loads(urllib.request.urlopen(url).read().decode())['data']
                target_date = parse(" ".join(new_comments[0]['permalink'].split('/')[-3].split("_")[-3:]))
                break
            except:
                print("Pushshift API call failed, trying again in 10 seconds...")


        filename = f"daily_comments/{target_date.date()}.txt"
        f = open(filename, "a", encoding='utf-8')
        for comment in new_comments:
            text = comment['body']
            text = text.replace("\n"," ")
            f.write(text+"\n")

        f.close()
    
    comment_ids_group = comment_ids[int(len(comment_ids)/1000)*1000:]
    url = f"https://api.pushshift.io/reddit/comment/search?ids={','.join(comment_ids_group)}"
    while True:
        try:
            new_comments = json.loads(urllib.request.urlopen(url).read().decode())['data']
            target_date = parse(" ".join(new_comments[0]['permalink'].split('/')[-3].split("_")[-3:]))
            break
        except:
            print("Pushshift API call failed, trying again in 10 seconds...")

    print(len(new_comments))

    filename = f"daily_comments/{target_date.date()}.txt"
    f = open(filename, "a", encoding='utf-8')
    for comment in new_comments:
        text = comment['body']
        text = text.replace("\n"," ")
        f.write(text+"\n")

    f.close()

        



if __name__ == "__main__":
    #target_date = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: "))) # datetime.datetime(2021, 1, 21) # 
    #get_daily_id(target_date=target_date)
    comment_ids = get_comment_ids("kjdkdk")
    pull_comments(comment_ids)

# This sucks because I found a way easier way to do this with pushshift instead of selenium webscraping
r"""

from selenium import webdriver
import datetime
from dateutil.parser import parse
from general_utils import log_error

def get_url(target_date=False):
    if target_date == False:
        target_date = datetime.date.today()
        print("No target_date supplied, defaulting to today.")

    url = f'https://www.reddit.com/r/wallstreetbets/search/?q=Daily%20Discussion%20Thread%20for%20{target_date.strftime("%B")}%20{str(int(target_date.strftime("%d")))}%2C%20{target_date.strftime("%Y")}&restrict_sr=1&sort=top'
    print(f"Search url: {url}")
    driver = webdriver.Chrome(executable_path=r'C:\Users\Gabe\Documents\programming\chromedriver.exe')
    driver.get(url)

    links = driver.find_elements_by_xpath('//*[@class="_eYtD2XCVieq6emjKBH3m"]')
    for a in links:
        if a.text.startswith('Daily Discussion Thread'):
            date = " ".join(a.text.split(' ')[-3:])
            parsed = parse(date) 
            if parse(str(target_date)) == parsed:
                link = str(a.find_element_by_xpath('../..').get_attribute('href'))
    
    driver.close()
    try:
        print(f"Daily discussion url: {link}")
        return(link)
    except:
        msg = f"Daily discussion thread for {target_date} not found. Is the market open on this date? Search url used: {url}"
        log_error(msg+"\n")
        raise Exception(msg)

if __name__ == "__main__":
    target_date = datetime.datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: "))) # datetime.datetime(2021, 1, 21) # 
    get_url
"""


# TODO: search top posts of the day and their comments