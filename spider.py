import urllib2
from bs4 import BeautifulSoup

html = urllib2.urlopen('http://www.pokeai.net/toz/dialga').read()
soup = BeautifulSoup(html, 'lxml')
print soup.get_text()
