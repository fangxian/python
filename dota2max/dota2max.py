from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
import json
import os
from Crawler import Crawler


def do_herocrawle(dotamax):
    dotamax.do_crawl_hero()


def do_itemcrawle(dotamax):
    pass


def do_matchcrawle():
    pass


def data_analyse():
    pass

def data_visualization():
    pass


if __name__ == '__main__':
    link = input("input the website to crawl:")
    dotamax_hero = Crawler("http://dotamax.com/player/hero/91698091/")
    do_herocrawle(dotamax_hero)
    for option in ["pro","vh"]:
        dotamax_item = Crawler("http://dotamax.com/player/items/91698091/?hero=55&skill="+option)
        do_itemcrawle(dotamax_item)