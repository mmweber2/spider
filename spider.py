#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen('http://www.pokeai.net/toz/dialga').read()
soup = BeautifulSoup(html, 'lxml', from_encoding="utf-8")
dialga = u"ディアルガ"
print dialga in soup.get_text()
