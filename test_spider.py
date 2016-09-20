from spider import Spider
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_no_links_http():
    start = "http://www.pokeai.net"
    result = Spider(start).crawl()
    assert_equals(result[0].links, [])
    assert_equals(len(result), 1)

def test_no_links_https():
    start = "https://www.google.com"
    result = Spider(start).crawl(1)
    assert start in [x.url for x in result]
    assert_equals(len(result), 2)

def test_many_links_choose_one():
    start = "http://www.yahoo.com"
    result = Spider(start).crawl(1)
    assert start in [x.url for x in result]
    assert_equals(len(result), 2)

def test_invalid_url_no_http():
    start = "www.yahoo.com"
    assert_raises(ValueError, Spider, start)

def test_invalid_url_number():
    assert_raises(AttributeError, Spider, 3)
