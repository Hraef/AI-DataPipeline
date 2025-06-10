import json
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

# Init
newsapi = NewsApiClient(api_key=api_key)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(language='en',country='us')

df = df[]
