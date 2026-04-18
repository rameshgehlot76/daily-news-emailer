# 📰 Daily News Emailer

An automated Python application that fetches the latest top headlines 
and delivers a beautifully formatted HTML email digest every morning 
— completely hands-free.

---

## 🚀 Features
- Fetches real-time top headlines using NewsAPI
- Sends beautifully formatted HTML emails
- Fully automated daily scheduling
- Modular and clean code architecture
- Supports Gmail SMTP with App Password authentication

---

## 🛠️ Tech Stack
| Technology | Purpose |
|------------|---------|
| Python 3 | Core language |
| NewsAPI | Fetching top headlines |
| smtplib | Sending emails via Gmail |
| MIME (email lib) | Building HTML email content |
| schedule | Daily automation |

---

## 📁 Project Structure 
daily_news_emailer/
│
├── config.py          # API keys and email credentials
├── news_fetcher.py    # Fetches headlines from NewsAPI
├── email_sender.py    # Builds and sends HTML email
├── main.py            # Entry point, runs the scheduler

---

## ⚙️ How It Works
1. `news_fetcher.py` calls NewsAPI and fetches top English headlines
2. `email_sender.py` builds a clean HTML email with the headlines
3. `main.py` runs the scheduler which triggers the email every morning
4. Gmail SMTP with App Password handles secure email delivery

---

## 📸 Sample Email Output
📰 Daily News Digest
━━━━━━━━━━━━━━━━━━━━

1. Headline one goes here...
2. Headline two goes here...
3. Headline three goes here... ━━━━━━━━━━━━━━━━━━━━ 
   Powered by NewsAPI + Python  

---

## 🔧 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/rameshgehlot76/daily-news-emailer.git
cd daily-news-emailer
```

### 2. Install dependencies
```bash
pip install requests schedule
```

### 3. Configure credentials
Edit `config.py` and add:
```python
NEWS_API_KEY = "your_newsapi_key"
EMAIL = "your_email@gmail.com"
PASSWORD = "your_gmail_app_password"
RECEIVER = "receiver@gmail.com"
```

### 4. Run the app
```bash
python main.py
```

---

## 🔑 Getting API Keys
- **NewsAPI** — Free key at [newsapi.org](https://newsapi.org)
- **Gmail App Password** — Enable 2FA on Gmail → Generate App Password

---

## 📚 What I Learned
- Working with REST APIs and JSON responses
- Sending HTML emails using Python's smtplib
- Building modular Python applications
- Automating tasks with the schedule library
- Handling API limitations and edge cases

---

## 👨‍💻 Author
**Ramesh Gehlot**  
[GitHub](https://github.com/rameshgehlot76)


