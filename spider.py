#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import urllib2
from bs4 import BeautifulSoup

def _contains_jp(text):
    """Returns True iff text contains Japanese hiragana/katakana characters."""
    for char in text:
        if (u'ぁ' <= char <= u'ん') or (u'ァ' <= char <= u'・'):
            return True

html = urllib2.urlopen('http://www.pokeai.net/toz/dialga').read()
soup = BeautifulSoup(html, 'lxml', from_encoding="utf-8")
dialga = u"ディアルガ"
print _contains_jp(soup.get_text())
