# 26th
# Daily News Emailer with Scheduled Time 
# Great Project! 


"""
## 📁 Project Structure    
```
daily_news_emailer/
│
├── config.py        # Your API keys & email settings
├── news_fetcher.py  # Fetches news from API
├── email_sender.py  # Builds & sends the email
└── main.py          # Scheduler - runs everything

1. One-Line Introduction (Say this First) 
  "I built a Daily News Emailer--a Python automation project that 
  fetches top news headlines from a live API and sends a beautifully 
  formatted HTML email every day at a scheduled time,automatically". 

2. Full Project Explanation (30-60 seconds) 
  "The project has 4 Python files. First, [config.py] stores all settings
  like email credentials and API keys. Second, [news_fetcher.py] makes an 
  API call to NewsAPI.org using the (requests) library and fetches the top 
  headlines based on category and country. Third, [email_sender.py] takes those
  articles and builds a professional HTML email with cards for each article, then 
  sends it using Python's built-in (smtplib) library over Gmail's SMTP server. Finally,
  [main.py] uses the (schedule) libbrary to run the whole thing automatically every day
  at a fix time."  
  
3. Technologies Used (Must mention these)
  Technology                   Why you used it
  [requests]               To call the NewsAPI and get JSON data
  [smtplib]                Python's built-in library to send emails
  [schedule]               To automate and run the task daily
  [MIME] (email library)   To build HTML formatted emails
  NewsAPI.org              Free REST API that gives live news data 
  Gmail SMTP               Email server used to deliver the mail


4. Common Interview Questions & Answers
    Q: What is an API? How did you use it here? 
  "An API is a way for two applications to talk to each other.
  Here, I used NewsAPI — I send an HTTP GET request with my API key,
  category, and country as parameters. It returns a JSON response with
  articles, and I extract the title, description, and URL from that JSON."

    Q: What is SMTP?
  "SMTP stands for Simple Mail Transfer Protocol.
  It's the standard protocol used to send emails over the internet.
  Python's smtplib library lets me connect to Gmail's SMTP server
  on port 465 and send emails programmatically."  

    Q: Why did you use an App Password instead of your Gmail password?
  "Google blocks direct password login for scripts for security reasons.
  App Passwords are special 16-character passwords generated specifically
  for third-party apps, so your main password stays safe."

    Q: How does scheduling work?
  "The schedule library lets you define jobs like schedule.
  every().day.at('08:00').do(job). Then I run a while True loop that checks
  every 60 seconds if any scheduled job is due, and runs it when the time matches."

    Q: What is JSON?
  "JSON stands for JavaScript Object Notation. It's a lightweight
  format used to exchange data between a server and a client.
  The NewsAPI returns news data in JSON format, and
  I parse it using Python's response.json() method."  

    Q: What challenges did you face?
  "One challenge was Gmail blocking normal password authentication.
  I solved it by enabling 2-step verification and using an App Password.
  Another challenge was formatting the HTML email to look clean — I used
  inline CSS since many email clients don't support external stylesheets."
 
  
5. How to Show Your Thinking (Impress the interviewer)
   Say this to stand out:
   "I structured the project in a modular way — separating config, news fetching,
   email sending, and scheduling into different files.  
   This makes it easy to maintain and extend. For example, 
   I can easily add a weather section or support multiple recipients just by modifying one file." 

🚀 6. How to Make it Sound Bigger
Add these lines if asked "can you improve this project?" 
"I can add a database to store sent articles and avoid duplicates"
"I can use keyword filtering so users only get news about topics they care about"
"I can deploy it on a cloud server like AWS or Heroku so it runs 24/7 without keeping my laptop on"
"I can add multiple recipients or even build a simple web form to subscribe/unsubscribe"

🗣️ Quick Summary to Memorize
Project     → Daily News Emailer
Language    → Python
Libraries   → requests, smtplib, schedule, email/MIME
API Used    → NewsAPI.org (REST API, returns JSON)
Sends via   → Gmail SMTP (port 465, SSL)
Runs        → Automatically every day at fixed time
Structure   → 4 files, modular design
"""  

