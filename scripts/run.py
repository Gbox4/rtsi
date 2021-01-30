import datetime
from scrape_daily import get_daily_id, get_comment_ids, pull_comments
from analyze_comments import analyze_daily


#target_date = datetime.date(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")))

for day in range(1,24):
    target_date = datetime.date(2020, 12, day)
    #print(f"Fetching comments for {day}")

    """try:
        comment_ids = get_comment_ids(get_daily_id(target_date=target_date))
    except Exception as e:
        if "Is the market open on this date?" in str(e):
            print("Thread not found, skipping...")
            continue
        else:
            raise e"""
    
    #pull_comments(comment_ids)

    analyze_daily(target_date)
