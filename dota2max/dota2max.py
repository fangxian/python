from Crawler import Crawler
import pandas as pd
import csv

def do_herocrawle(dotamax):
    dotamax.do_crawl_hero()


def do_itemcrawle(dotamax_item, option):
    dotamax_item.do_crawl_item(option)


def do_matchcrawle():
    pass


def data_analyse():
    pass

def data_visualization():
    pass


if __name__ == '__main__':
    pro_name = input("input the player name:")
    link = input("input the website to crawl:")
    dotamax_hero = Crawler(link, pro_name)
    do_herocrawle(dotamax_hero)
    #do not include the pro and vh in the item link
    item_link = input("input item link:")
    for option in ["pro", "vh"]:
        dotamax_item = Crawler(item_link+option, pro_name)
        do_itemcrawle(dotamax_item, option)