import datetime
from scrape_daily import get_daily_id, get_comment_ids, pull_comments
from analyze_comments import analyze_daily
import pathlib
import sqlite3
current_directory = str(pathlib.Path(__file__).parent.absolute())
import re
import time
start_time = time.time()


for day in range(10,24):
    analyze_daily(datetime.date(2020,12,day))


"""for ticker in [tup[0] for tup in list(c.execute("SELECT ticker FROM ticker_metadata WHERE LENGTH(ticker)=1;"))]:
    if not re.search(f'\${ticker.lower()}(\\W|$)',all_text):
        print(ticker)
        c.execute(f"UPDATE ticker_metadata SET obscure=1 WHERE ticker=?", (ticker,))"""


"""for ticker in [tup[0] for tup in list(c.execute("SELECT ticker FROM ticker_metadata WHERE NOT common_word"))]:
    if list(c.execute("SELECT COUNT(*) FROM daily_discussion_comment_data WHERE LOWER(text) REGEXP ?", (f'(^|\\W){ticker.lower()}(\\W|$)', )))[0][0] == 0:
        print(ticker)
    if i == 20: print(time.time() - start_time)
    i += 1
        #c.execute(f"UPDATE ticker_metadata SET obscure=1 WHERE ticker={ticker}")

for ticker in [tup[0] for tup in list(c.execute("SELECT ticker FROM ticker_metadata WHERE common_word"))]:
    if list(c.execute("SELECT COUNT(*) FROM daily_discussion_comment_data WHERE LOWER(text) REGEXP ?", (f'\${ticker.lower()}(\\W|$)', )))[0][0] == 0:
        print(ticker)
        #c.execute(f"UPDATE ticker_metadata SET obscure=1 WHERE ticker={ticker}")"""


#conn.commit()
#conn.close()