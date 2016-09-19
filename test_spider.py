from spider import Spider

def test_no_links():
    start = "http://www.pokeai.net"
    spider = Spider(start)
    print spider.crawl()
