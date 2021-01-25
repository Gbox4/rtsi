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
    with open(f"{current_directory}/../data/nasdaqlisted.txt", "r") as f:
        for line in f:
            tickers.append(line.split("|")[0].lower())

    common_words = []
    f = open(f"{current_directory}/../data/common_words.txt", "r")
    for line in f:
        common_words.append(line.replace("\n", "").lower())

    comments = []
    
    f = open(f"{current_directory}/../data/daily_comments/{target_date}.txt", "r", encoding="utf-8")
    for line in f:
        comments.append(line.replace("\n", "").lower())

    ticker_frequency = {}

    tickers = np.array(tickers)
    comments = np.array(comments)
    for comment in comments:
        for ticker in tickers:
            if ticker in comment:
                # If its a common word, perform a stricter search
                if ticker in common_words:
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
    
    return ticker_frequency

if __name__ == "__main__":
    print(analyze_daily(datetime.date(2020,12,24)))


# TODO: remove bot comments