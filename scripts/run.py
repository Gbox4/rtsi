import datetime
from scrape_daily import get_daily_id, get_comment_ids, pull_comments
from analyze_comments import analyze_daily
import pathlib
import sqlite3
current_directory = str(pathlib.Path(__file__).parent.absolute())



conn = sqlite3.connect(f"{current_directory}/../tickerdat.db")
c = conn.cursor()





conn.commit()
conn.close()