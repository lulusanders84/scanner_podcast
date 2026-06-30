import requests

ENDPOINT = "https://junctionnow.com/wp-json/do-spaces/v1/list"
PREFIX = "2026/06-30-26/05/Police Dispatch/"


def walk(prefix=""):
    r = requests.get(
        ENDPOINT,
        params={
            "prefix": prefix,
            "limit": 1000,
        },
    )

    r.raise_for_status()
    data = r.json()

    # Visit subfolders
    for sub in data["prefixes"]:
        # Depending on the API, this may be a string or a dict.
        next_prefix = sub if isinstance(sub, str) else sub["prefix"]
        yield from walk(next_prefix)

    # Yield files
    yield from data["files"]
