import xml.etree.ElementTree as ET
from datetime import datetime, timezone


def create_feed(articles):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "Corey Cesare - Articles"
    ET.SubElement(channel, "link").text = "https://talentrecap.com/author/corey-cesare/"
    ET.SubElement(channel, "description").text = "Latest articles by Corey Cesare"
    ET.SubElement(channel, "language").text = "en-us"

    for article in articles:
        item = ET.SubElement(channel, "item")

        ET.SubElement(item, "title").text = article["title"]
        ET.SubElement(item, "link").text = article["link"]
        ET.SubElement(item, "description").text = article.get("description", "")
        ET.SubElement(item, "pubDate").text = article["date"]

    tree = ET.ElementTree(rss)

    with open("feed.xml", "wb") as file:
        tree.write(
            file,
            encoding="utf-8",
            xml_declaration=True
        )


if __name__ == "__main__":
    articles = [
        {
            "title": "Corey Cesare Articles",
            "link": "https://talentrecap.com/author/corey-cesare/",
            "description": "Latest entertainment journalism by Corey Cesare.",
            "date": datetime.now(timezone.utc).strftime(
                "%a, %d %b %Y %H:%M:%S GMT"
            )
        }
    ]

    create_feed(articles)
