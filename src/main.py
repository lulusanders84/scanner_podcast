import json
import re
import xml.etree.ElementTree as ET

from src.rss_feed import create_feed
from src.url_list import retrieve, get_url_list_filename
from src.walk import walk


PREFIX = "2026/06-30-26/04"
EXAMPLE = "https://junctionnow-audio.sfo3.digitaloceanspaces.com/2026/06-29-26/00/CSP%20Troop%204A/20260629_003457_State-of-Colorado-DTRS_Mesa_T-Control__TO_P8102_FROM_547073.mp3"


def get_new_string_and_prefix(string, pattern):
    m = re.search(pattern, string)
    if m:
        return [string[m.end() + 1:], get_url_list_filename(m.group()[1:])]

def get_date(string):
    return get_new_string_and_prefix(string, re.compile(r"/[0-9]{4}/[0-9]{2}-[0-9]{2}-[0-9]{2}"))


def get_hour(string):
    return get_new_string_and_prefix(string, re.compile(r"/[0-9]{2}"))


def get_channel(string):
    return get_new_string_and_prefix(string, re.compile(r"/[^/]*"))


def convert_to_dicts(url_list):
    url_dicts = []
    for url in url_list:
        [string, date] = get_date(url)
        [hour, channel, file] = string.split("/")
        url_dicts.append({"date": date, "hour": hour, "channel": channel, "file": file, "url": url})
    return url_dicts


def main():
    # create_url_list(PREFIX)

    with open("output.json", 'r') as f:
        data = json.load(f)

    tree = create_feed(data, "06-30-26 0400")

    ET.indent(tree, space="  ")  # Python 3.9+
    tree.write(
        "0400_feed.xml",
        encoding="utf-8",
        xml_declaration=True,
    )
    pass

main()