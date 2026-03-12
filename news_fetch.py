import feedparser
import json

feeds = [
    "https://finance.yahoo.com/rss/topstories",
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "https://www.marketwatch.com/rss/topstories"
]

news = []

for feed in feeds:
    data = feedparser.parse(feed)
    for entry in data.entries[:5]:
        news.append({
            "title": entry.title,
            "link": entry.link
        })

with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)

print("News updated")
