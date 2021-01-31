import datetime
from scrape_daily import get_daily_id, get_comment_ids, pull_comments
from analyze_comments import analyze_daily
import pathlib
import sqlite3
current_directory = str(pathlib.Path(__file__).parent.absolute())


#target_date = datetime.date(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))

"""for day in range(1,5):
    target_date = datetime.date(2020, 12, day)
    analyze_daily(target_date)"""

common_words = []
f = open(f"{current_directory}/../data/common_words.txt", "r")
for line in f:
    common_words.append(line.replace("\n", ""))
f.close()

conn = sqlite3.connect(f"{current_directory}/../tickerdat.db")
c = conn.cursor()

with open(f"{current_directory}/../data/nasdaq_tickers.csv", "r") as f:
    for line in f:
        ticker = line.split(",")[0]
        common_word = ticker in common_words
        exchange = "NASDAQ"
        obscure = False
        c.execute(f"INSERT INTO ticker_metadata VALUES (?,?,?,?)", (ticker,common_word,exchange,obscure))


with open(f"{current_directory}/../data/nyse_tickers.csv", "r") as f:
    for line in f:
        ticker = line.split(",")[0]
        common_word = ticker in common_words
        exchange = "NYSE"
        obscure = False
        c.execute(f"INSERT INTO ticker_metadata VALUES (?,?,?,?)", (ticker,common_word,exchange,obscure))


conn.commit()
conn.close()