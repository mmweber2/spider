#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import urllib2
import MeCab
import sys
from bs4 import BeautifulSoup

class Page(object):
    """Represents a single web page."""

    def __init__(self, url, text, links):
        """Creates a new Page.

        text and links are determined by parsing the page with Beautiful Soup 4.

        Args:
            url: string, the absolute URL at which this page was found.

            text: string, the text of this page. May contain some html, xml,
                CSS code, or other formatting, but is intended to be text only.

            links: list, a list of absolute URL links found on the page.
        """
        self.url = url
        self.text = text
        self.links = links

    def __str__(self):
        return u"URL: {}\nFirst 100 characters of text: {}\n\nLinks: {}".format(
                self.url, self.text.strip()[:100], self.links)

def _parse_page(url):
    """Creates a new Page by retrieving and parsing the given url."""
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml', from_encoding="utf-8")
    #contents = [x.get('content') for x in soup.find_all('meta')]
    links = [link.get('href') for link in soup.find_all('a')]
    return Page(url, soup.get_text(), links)

def _contains_jp(texts):
    """Returns True iff texts contains Japanese hiragana/katakana characters."""
    for text in texts:
        for char in text:
            if (u'ぁ' <= char <= u'ん') or (u'ァ' <= char <= u'・'):
                return True
    return False

page = _parse_page('http://www.yahoo.co.jp')
print page.__str__()
#print _contains_jp(page.text)


# TODO: Get MeCab parsing working within program
#mecab = MeCab.Tagger(" ".join(sys.argv))
#words = mecab.parse(text)
#print words
