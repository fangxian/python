from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
import json
import os
from Crawler import Crawler


def do_herocrawle(dotamax):
    dotamax.do_crawl_hero()

if __name__ == '__main__':
    dotamax = Crawler("http://dotamax.com/player/hero/91698091/")
    do_herocrawle(dotamax)
