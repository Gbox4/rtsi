import re
import numpy as np
import time
import pathlib
start_time = time.time()
current_directory = str(pathlib.Path(__file__).parent.absolute())

tickers = []
with open(f"{current_directory}/data/nasdaqlisted.txt", "r") as f:
    for line in f:
        tickers.append(line.split("|")[0].lower())


comments = []
f = open(f"{current_directory}/data/daily_comments/2020-12-24.txt", "r", encoding="utf-8")
for line in f:
    comments.append(line.replace("\n", "").lower())


ticker_frequency = {}

i = 1
tickers = np.array(tickers)
comments = np.array(comments)
for comment in comments:
    for ticker in tickers:
        if ticker in comment:
            if re.search(f"(^|\\W){ticker}(\\W|$)",comment):
                try:
                    ticker_frequency[ticker] += 1
                except:
                    ticker_frequency[ticker] = 1
    
    i += 1

print(ticker_frequency)
print("--- %s seconds ---" % (time.time() - start_time))