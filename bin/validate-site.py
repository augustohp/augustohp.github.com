#!/usr/bin/env python3
"""Smoke-check the production Jekyll output without extra dependencies."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.tags = []
        self.text = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


def require(condition, message):
    if not condition:
        raise SystemExit(message)


site = Path("_site")
atom = ET.parse(site / "atom.xml").getroot()
ns = {"a": "http://www.w3.org/2005/Atom"}
require(atom.tag == "{http://www.w3.org/2005/Atom}feed", "Not an Atom feed")
home_link = atom.find("a:link[@rel='alternate']", ns)
require(home_link is not None, "Atom homepage link missing")
site_url = urlsplit(home_link.get("href", ""))
require(site_url.scheme in ("http", "https") and site_url.netloc,
        "Atom homepage URL not absolute")
prefix = site_url.path.rstrip("/")


def output_path(path):
    require(path.startswith(prefix + "/"), f"URL outside site base path: {path}")
    relative = unquote(path[len(prefix):]).lstrip("/")
    return site / (relative + "index.html" if path.endswith("/") else relative)


home = Page(site / "index.html")
archive = Page(site / "posts/index.html")
require("Últimos posts" in " ".join(home.text), "Homepage title missing")
require("Todos os posts" in " ".join(archive.text), "Archive title missing")

# An old, stable post exercises dated/category permalinks and Markdown content.
posts = list(site.glob("**/novo-blog.html"))
require(len(posts) == 1, "Representative post missing or duplicated")
post = Page(posts[0])
require("Novo (mentira) Blog" in " ".join(post.text), "Post title missing")
require("Wordpresse e Habari" in " ".join(post.text), "Post content missing")
post_path = prefix + "/" + posts[0].relative_to(site).as_posix()
require(any(tag == "a" and urlsplit(attrs.get("href", "")).path == post_path
            for tag, attrs in archive.tags), "Archive does not link to the post")

styles = [attrs["href"] for tag, attrs in home.tags
          if tag == "link" and "stylesheet" in attrs.get("rel", "").split()]
local_styles = [urlsplit(url).path for url in styles
                if urlsplit(url).netloc in ("", site_url.netloc)]
require(local_styles, "Homepage has no local stylesheet")
for path in local_styles:
    css = output_path(path).read_text()
    require("{" in css and "}" in css, f"Stylesheet empty or uncompiled: {path}")

entries = atom.findall("a:entry", ns)
require(entries, "Atom feed has no posts")
for entry in entries:
    require(entry.findtext("a:title", namespaces=ns), "Atom entry title missing")
    link = entry.find("a:link[@rel='alternate']", ns)
    require(link is not None, "Atom entry permalink missing")
    url = urlsplit(link.get("href", ""))
    require(url.scheme in ("http", "https") and url.netloc, "Atom URL not absolute")
    require(output_path(url.path).is_file(),
            f"Atom links to missing post: {url.path}")

sitemap = ET.parse(site / "sitemap.xml").getroot()
require(sitemap.tag == "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset",
        "Not a sitemap")
locations = sitemap.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/"
                            "{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
urls = [urlsplit(location.text or "") for location in locations]
require(all(url.scheme in ("http", "https") and url.netloc for url in urls),
        "Sitemap URL not absolute")
require({prefix + "/", prefix + "/posts/", post_path} <= {url.path for url in urls},
        "Sitemap missing homepage, archive, or representative post")

# Disqus thread keys predate the site's HTTPS migration. Check both an encoded
# historical permalink and the latest post's custom, trailing-slash permalink.
comment_paths = ["/php,%20jardinagem/2011/07/28/mvc-errado.html",
                 urlsplit(entries[0].find("a:link[@rel='alternate']", ns).get("href")).path]
for path in comment_paths:
    page = Page(output_path(path))
    require(sum(attrs.get("id") == "disqus_thread" for _, attrs in page.tags) == 1,
            f"Disqus container missing or duplicated: {path}")
    script = "\n".join(page.text)
    require("https://augustopascuttisblog.disqus.com/embed.js" in script,
            f"Historical Disqus forum missing: {path}")
    thread_url = json.dumps("http://blog.augustopascutti.com" + path)
    for setting in ("url", "identifier"):
        require(f"this.page.{setting} = {thread_url};" in script,
                f"Historical Disqus {setting} changed: {path}")
    require(any(tag == "link" and attrs.get("rel") == "canonical"
                and attrs.get("href") == "https://blog.augustopascutti.com" + path
                for tag, attrs in page.tags), f"HTTPS canonical changed: {path}")
for page in (home, archive):
    require(not any(attrs.get("id") == "disqus_thread" for _, attrs in page.tags),
            "Disqus must only appear on posts")

print("PASS: homepage, archive, post, CSS, Atom entries, sitemap, and historical Disqus keys")
