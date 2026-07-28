import requests
import html

SOURCE_FEED = "https://talentrecap.com/author/corey-cesare/feed/"
OUTPUT_FILE = "feed.xml"

response = requests.get(
    SOURCE_FEED,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

response.raise_for_status()

feed = response.text

# Convert HTML entities into safe XML text
feed = html.unescape(feed)

# Escape ampersands that are not already XML-safe
feed = feed.replace("&", "&amp;")
feed = feed.replace("&amp;amp;", "&amp;")

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(feed)

print("Clean RSS feed created!")
