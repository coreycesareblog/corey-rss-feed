import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import formatdate
from html import escape


def format_rss_date(date_string):
    """
    Converts WordPress ISO dates into RSS-friendly dates.
    Example:
    2026-07-23T15:00:00 -> Thu, 23 Jul 2026 15:00:00 GMT
    """
    try:
        dt = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        return formatdate(dt.timestamp(), usegmt=True)
    except Exception:
        return formatdate(datetime.now().timestamp(), usegmt=True)


def create_feed(articles):
    rss = ET.Element("rss", {
        "version": "2.0",
        "xmlns:atom": "http://www.w3.org/2005/Atom",
        "xmlns:media": "http://search.yahoo.com/mrss/"
    })

    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = "Corey Cesare - Articles"
    ET.SubElement(channel, "link").text = "https://talentrecap.com/author/corey-cesare/"
    ET.SubElement(channel, "description").text = "Latest articles by Corey Cesare"
    ET.SubElement(channel, "language").text = "en-us"

    ET.SubElement(channel, "atom:link", {
        "href": "https://coreycesareblog.github.io/corey-rss-feed/feed.xml",
        "rel": "self",
        "type": "application/rss+xml"
    })

    ET.SubElement(
        channel,
        "lastBuildDate"
    ).text = formatdate(datetime.now().timestamp(), usegmt=True)


    for article in articles:
        item = ET.SubElement(channel, "item")

        ET.SubElement(
            item,
            "title"
        ).text = article.get("title", "Untitled")

        ET.SubElement(
            item,
            "link"
        ).text = article.get("link", "")

        ET.SubElement(
            item,
            "guid"
        ).text = article.get("link", "")


        description = article.get(
            "excerpt",
            "Read the full article on Talent Recap."
        )


        # Add featured image for Feedzy and RSS readers
        if article.get("image"):
            image_url = article["image"]

            ET.SubElement(
                item,
                "{http://search.yahoo.com/mrss/}content",
                {
                    "url": image_url,
                    "medium": "image"
                }
            )

            ET.SubElement(
                item,
                "{http://search.yahoo.com/mrss/}thumbnail",
                {
                    "url": image_url
                }
            )

            description = (
                f'<img src="{image_url}" />'
                + description
            )


        ET.SubElement(
            item,
            "description"
        ).text = escape(description)


        ET.SubElement(
            item,
            "pubDate"
        ).text = format_rss_date(article.get("date", ""))


    tree = ET.ElementTree(rss)

    ET.indent(tree, space="  ")

    tree.write(
        "feed.xml",
        encoding="UTF-8",
        xml_declaration=True
    )


# Keep compatibility if runfeed.py imports this name
generate_feed = create_feed
