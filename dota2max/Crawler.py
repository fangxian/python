from urllib.request import urlopen
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, link):
        self.link = link

    def get_link(self):
        html = urlopen(self.link)
        bs_obj = BeautifulSoup(html.read())
        s = bs_obj.findAll("td")
        print(s[1].get_text())
        #print(s.get_text())

    def do_crawl_hero(self, hero):
        pass

    def do_crawl_item(self, item):
        pass

    def do_crawl_match(self, match):
        pass

    def save_data(self, data):
        pass