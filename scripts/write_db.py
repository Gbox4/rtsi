from analyze_comments import analyze_daily
import datetime
import sqlite3
import pathlib
current_directory = str(pathlib.Path(__file__).parent.absolute())

target_date = datetime.date(2020,12,24)
analysis_result = analyze_daily(target_date)


tickers = []
with open(f"{current_directory}/../data/nasdaqlisted.txt", "r") as f:
    for line in f:
        tickers.append(line.split("|")[0])

conn = sqlite3.connect(f"{current_directory}/../tickerdat.db")
c = conn.cursor()
for ticker in tickers:
    if ticker in list(analysis_result.keys()):
        frequency = analysis_result[ticker]
        c.execute(f"INSERT INTO daily_discussion_ticker_data VALUES (?,?,?)", (str(target_date),ticker,frequency))

conn.commit()
conn.close()