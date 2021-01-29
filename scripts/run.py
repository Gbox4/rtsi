import datetime
from scrape_daily import get_daily_id, get_comment_ids, pull_comments
from analyze_comments import analyze_daily


target_date = datetime.date(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))
#comment_ids = get_comment_ids(get_daily_id(target_date=target_date))
#pull_comments(comment_ids)
analyze_daily(target_date)