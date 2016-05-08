from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import pandas as pd
import json
import os
from Crawler import Crawler


def createcrawler():
    dotamax = Crawler("http://dotamax.com/player/hero/91698091/")
    dotamax.get_link()

if __name__ == '__main__':
    createcrawler()
