import requests

SOURCE_FEED = "https://talentrecap.com/author/corey-cesare/feed/"
OUTPUT_FILE = "feed.xml"


response = requests.get(
    SOURCE_FEED,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

response.raise_for_status()

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(response.text)

print("RSS feed copied successfully!")
