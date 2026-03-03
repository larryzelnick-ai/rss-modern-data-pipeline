import feedparser
import pandas as pd

feed_name = "nytimes"   # or whatever RSS source you are pulling from
url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"

feed = feedparser.parse(url)

rows = []

for entry in feed.entries:
    rows.append({
        "title": entry.get("title"),
        "published": entry.get("published"),
        "link": entry.get("link"),
        "summary": entry.get("summary"),
        "source_feed": feed_name   # or feed URL/domain name
    })

df = pd.DataFrame(rows)

df.to_csv("rss_modernization/data/rss_raw.csv", index=False)

print("RSS data extracted -> rss_modernization/data/rss_raw.csv")
