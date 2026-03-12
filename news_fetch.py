import feedparser
import json

sources = {
    "yahoo":"https://finance.yahoo.com/news/rssindex",
    "cnbc":"https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "marketwatch":"https://feeds.marketwatch.com/marketwatch/topstories/"
}

news=[]

for name,url in sources.items():
    feed = feedparser.parse(url)

    for entry in feed.entries[:5]:

        news.append({
            "title":entry.title,
            "link":entry.link,
            "source":name
        })

with open("news.json","w",encoding="utf-8") as f:
    json.dump(news,f,ensure_ascii=False,indent=2)
