# Build & Send Beautiful HTML Email 

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from config import SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL 

def build_html(articles):
    today = datetime.now().strftime("%A, %d %B %Y")
    category = "Technology"

    # Build one card per article
    cards_html = ""
    for i, article in enumerate(articles, 1):
        cards_html += f"""
        <div style="background:#fff; border-left: 4px solid #4F46E5;
                    margin-bottom:20px; padding:16px; border-radius:6px;
                    box-shadow: 0 1px 4px rgba(0,0,0,0.08);">
            <p style="margin:0 0 4px 0; color:#888; font-size:12px;">
                #{i} &nbsp;|&nbsp; {article['source']} &nbsp;|&nbsp; {article['publishedAt']}
            </p>
            <h3 style="margin:0 0 8px 0; color:#1a1a2e; font-size:16px;">
                {article['title']}
            </h3>
            <p style="margin:0 0 12px 0; color:#555; font-size:14px; line-height:1.5;">
                {article['description']}
            </p>
            <a href="{article['url']}"
               style="color:#4F46E5; font-size:13px; text-decoration:none; font-weight:600;">
                Read Full Article →
            </a>
        </div>
        """

    html = f"""
    <html>
    <body style="margin:0; padding:0; background:#f4f4f8; font-family: 'Segoe UI', Arial, sans-serif;">
      <div style="max-width:620px; margin:30px auto; background:#f4f4f8;">

        <!-- HEADER -->
        <div style="background: linear-gradient(135deg, #4F46E5, #7C3AED);
                    padding:30px; border-radius:10px 10px 0 0; text-align:center;">
          <h1 style="margin:0; color:#fff; font-size:26px;">📰 Daily News Digest</h1>
          <p style="margin:8px 0 0 0; color:#c4b5fd; font-size:14px;">{today}</p>
          <span style="display:inline-block; margin-top:10px; background:rgba(255,255,255,0.2);
                       color:#fff; padding:4px 14px; border-radius:20px; font-size:12px;">
            {category} News
          </span>
        </div>

        <!-- BODY -->
        <div style="background:#f4f4f8; padding:24px;">
          <p style="color:#555; font-size:14px; margin:0 0 20px 0;">
            Good morning! Here are your top {len(articles)} {category} headlines for today. ☕
          </p>

          {cards_html}
        </div>

        <!-- FOOTER -->
        <div style="background:#1a1a2e; padding:18px; border-radius:0 0 10px 10px; text-align:center;">
          <p style="margin:0; color:#888; font-size:12px;">
            Automated Daily News Emailer &nbsp;|&nbsp; Built with Python 🐍
          </p>
          <p style="margin:4px 0 0 0; color:#666; font-size:11px;">
            Powered by NewsAPI.org
          </p>
        </div>

      </div>
    </body>
    </html>
    """
    return html


def send_news_email(articles):
    if not articles:
        print("⚠️  No articles to send.")
        return

    today = datetime.now().strftime("%d %B %Y")

    msg = MIMEMultipart("alternative")
    msg["From"]    = SENDER_EMAIL
    msg["To"]      = RECEIVER_EMAIL
    msg["Subject"] = f"📰 Daily News Digest — {today}"

    html_content = build_html(articles)
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"✅ News email sent at {datetime.now().strftime('%I:%M %p')}")
    except Exception as e:
        print(f"❌ Error sending email: {e}")  
        


 
