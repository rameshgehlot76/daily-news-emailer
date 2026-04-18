# The Scheduler - runs everything 

import schedule
import time
from news_fetcher import fetch_news
from email_sender import send_news_email
from config import SEND_TIME 

def job():
    print("📡 Fetching latest news...")
    articles = fetch_news()
    print(f"✅ Got {len(articles)} articles. Sending email...") 
    send_news_email(articles) 
    
# Schedule the job 
schedule.every().day.at(SEND_TIME).do(job) 

print(f"🗞️ Daily News Emailer started!") 
print(f"📬 Email will be sent every day at {SEND_TIME}")  
print("   Press Ctrl+C to stop.\n") 

# Run once immediately to test 
job() 

"""
# Keep running
while True:
    schedule.run_pending()
    time.sleep(60) 
""" 

