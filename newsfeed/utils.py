# newsfeed/utils.py

import requests

def fetch_google_news(query, api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    news_items = []

    for article in articles:
        news_items.append({
            'title': article['title'],
            'content': article['description'],
            'source_url': article['url'],
            'published_date': article['publishedAt']
        })

    return news_items
