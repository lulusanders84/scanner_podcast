from datetime import datetime
from email.utils import format_datetime
import xml.etree.ElementTree as ET


def create_feed(files, title):
    rss = ET.Element(
        "rss",
        {
            "version": "2.0",
            "xmlns:atom": "http://www.w3.org/2005/Atom",
            "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        },
    )

    channel = ET.SubElement(rss, "channel")

    ET.SubElement(channel, "title").text = title
    ET.SubElement(channel, "link").text = "https://example.com/"
    ET.SubElement(channel, "description").text = "Personal scanner feed"
    ET.SubElement(channel, "language").text = "en-us"

    for file in files:
        item = ET.SubElement(channel, "item")

        ET.SubElement(item, "title").text = file["name"]

        guid = ET.SubElement(item, "guid")
        guid.set("isPermaLink", "false")
        guid.text = file["name"]

        dt = datetime.fromisoformat(file["last_modified"])
        ET.SubElement(item, "pubDate").text = format_datetime(dt)

        enclosure = ET.SubElement(item, "enclosure")
        enclosure.set("url", file["url"])
        enclosure.set("length", str(file["size"]))
        enclosure.set("type", "audio/mpeg")

    return ET.ElementTree(rss)