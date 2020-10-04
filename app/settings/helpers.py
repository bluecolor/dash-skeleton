import os
from tssplit import tssplit
from urllib.parse import urlparse, urlunparse

def parse_boolean(s):
    """Takes a string and returns the equivalent as a boolean value."""
    s = s.strip().lower()
    if s in ("yes", "true", "on", "1"):
        return True
    elif s in ("no", "false", "off", "0", "none"):
        return False
    else:
        raise ValueError("Invalid boolean value %r" % s)

def array_from_string(s, sep=","):
    array = s.split(sep)
    if "" in array:
        array.remove("")

    return array

def add_decode_responses_to_redis_url(url):
    """Make sure that the Redis URL includes the `decode_responses` option."""
    parsed = urlparse(url)

    query = "decode_responses=True"
    if parsed.query and "decode_responses" not in parsed.query:
        query = "{}&{}".format(parsed.query, query)
    elif "decode_responses" in parsed.query:
        query = parsed.query

    return urlunparse(
        [
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            parsed.params,
            query,
            parsed.fragment,
        ]
    )

def fix_assets_path(path):
    fullpath = os.path.join(os.path.dirname(__file__), "../", path)
    return fullpath


def set_from_string(s, sep=","):
    return set(array_from_string(s, sep))


def string_to_array(s, delimiter=",", quote='"', strip=True, escape="^"):
    return [token.strip() if strip else token for token in  tssplit(s, quote=quote, delimiter=delimiter, escape=escape)]

def string_to_set(s, delimiter=",", quote='"', strip=True, escape="^"):
    return set(string_to_array(s, delimiter, quote, strip, escape))


def is_in_urls(urls, url):
    p = urlparse(url)
    for u in urls:
        _p = urlparse(u)
        if _p.scheme == p.scheme and _p.netloc == p.netloc:
            return True

    return False