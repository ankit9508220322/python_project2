import requests
import json

query = input("write city name: ")

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey=32b571d3cc3d4e5a933a5b469c5d23e7"

r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print(".........................................")