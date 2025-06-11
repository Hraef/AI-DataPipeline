import json
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
import pandas as pd


load_dotenv()
api_key = os.getenv('API_KEY')

# Init
newsapi = NewsApiClient(api_key=api_key)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en',country='us')


#df = pd.DataFrame(top_headlines)
#df.to_csv('output.csv', index=False)
articles = top_headlines.get('articles', [])
df = pd.DataFrame([{
    'title': a.get('title'),
    'description': a.get('description'),
    'content': a.get('content'),
    'source': a.get('source', {}).get('name'),
    'publishedAt': a.get('publishedAt')
    } for a in articles])

df.to_csv('output.csv', index=False)
#titles = [article['title'] for article in articles]

#for i, title in enumerate(titles, 1):
#    print(f"{i}. {title}")


