#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import urllib2
import MeCab
from bs4 import BeautifulSoup

def _contains_jp(texts):
    """Returns True iff texts contains Japanese hiragana/katakana characters."""
    for text in texts:
        for char in text:
            if (u'ぁ' <= char <= u'ん') or (u'ァ' <= char <= u'・'):
                return True
    return False

html = urllib2.urlopen('http://www.yahoo.co.jp').read()
soup = BeautifulSoup(html, 'lxml', from_encoding="utf-8")
contents = [x.get('content') for x in soup.find_all('meta')]
print _contains_jp(contents)

#mecab = MeCab.Tagger()
#words = mecab.parseToNode(text)
#print mecab.parse(soup.get_text()[:50])
