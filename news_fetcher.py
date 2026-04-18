# Fetch News from API

import requests 
from config import NEWS_API_KEY 

def fetch_news():
    #print(f"API Key: {NEWS_API_KEY}")  # Debugging line to check if API key is loaded correctly 
    url = "https://newsapi.org/v2/top-headlines" 
    
    params = {
        "apiKey"   : NEWS_API_KEY,
        "category" : "technology",   # or "general" 
        "language" : "en",           # use language, NOT country 
        "pageSize" : 5 
    } 
    
    response = requests.get(url, params=params) 
    data = response.json() 
    return data.get("articles", []) 
  #  print("Status code", response.status_code)  # Debugging line to check API response status 
  #  print("Response:", response.json())  # Debugging line to check API response content  
    
    articles = [] 
    for article in data["articles"]:
        articles.append({
            "title"       : article.get("title", "No Title"),
            "description" : article.get("description", "No description available."),
            "url"         : article.get("url", "#"),
            "source"      : article.get("source", {}).get("name", "Unknown"),
            "publishedAt" : article.get("publishedAt", "")[:10]    # Only date part 
            
        }) 
        
    return articles 






        
        