import re
import numpy as np
import datetime
import time
import pathlib
import sqlite3
start_time = time.time()
current_directory = str(pathlib.Path(__file__).parent.absolute())

def analyze_daily(target_date):
    print(f"Analyzing {str(target_date)}")
    tickers = []
    with open(f"{current_directory}/../data/ticker_list.txt", "r") as f:
        for line in f:
            ticker = line.split(" ")[-1].replace("\n", '')
            if not ticker.isnumeric() and ticker.isupper(): tickers.append(ticker.lower())

    common_words = []
    f = open(f"{current_directory}/../data/common_words.txt", "r")
    for line in f:
        common_words.append(line.replace("\n", "").lower())
    f.close()

    ignore_authors = []
    f = open(f"{current_directory}/../data/ignore_authors.txt", "r")
    for line in f:
        ignore_authors.append(line.replace("\n", ""))
    f.close()

    append_sql_cmd = ""
    append_sql_args = []
    for author in ignore_authors:
        append_sql_cmd += f" AND NOT author=?"
        append_sql_args.append(author)

    conn = sqlite3.connect(f"{current_directory}/../tickerdat.db")
    c = conn.cursor()
    
    i=0
    ticker_frequency = {}

    for ticker in tickers:
        # Constructing the SQL query
        comments = list(c.execute("SELECT text FROM daily_discussion_comment_data WHERE date=? AND text LIKE ?" + append_sql_cmd, (str(target_date), f"%{ticker}%", *append_sql_args)))
        for comment in comments:
            comment = comment[0].lower()
            # If its a common word, perform a stricter search
            if ticker in common_words or len(ticker) == 1:
                if re.search(f"\${ticker}(\\W|$)",comment):
                    try:
                        ticker_frequency[ticker.upper()] += 1
                    except:
                        ticker_frequency[ticker.upper()] = 1
            else:
                if re.search(f"(^|\\W){ticker}(\\W|$)",comment):
                    try:
                        ticker_frequency[ticker.upper()] += 1
                    except:
                        ticker_frequency[ticker.upper()] = 1
                

        i+=1
        if i%1000 == 0: print(i)
    
    # Put the data into db
    for ticker, frequency in ticker_frequency.items():
        c.execute(f"INSERT INTO daily_discussion_ticker_data VALUES (?,?,?)", (str(target_date),ticker,frequency))
    
    conn.commit()
    conn.close()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    analyze_daily(datetime.date(2020,12,24))


# TODO: remove bot comments