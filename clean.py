import pandas as pd
import os


df = pd.read_csv('output.csv')
df = df.dropna(subset=['title', 'description'])
df['content'] = df['content'].fillna('')

df = df.drop_duplicates(subset=['title'])

df['text'] = df['title'] + '' + df['description'] + '' + df['content']

df['text'] = df['text'].str.lower()
df['text'] = df['text'].str.replace(r'\s+', '', regex=True)
df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)

df = df[df['text'].str.len() > 50]

df.to_csv('cleanedData.csv', index=False)
