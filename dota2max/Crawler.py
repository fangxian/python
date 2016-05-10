from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import os


class Crawler:
    def __init__(self, link, pro_name):
        self.link = link
        self.name = pro_name

    def do_crawl_hero(self):
        html = urlopen(self.link)
        bs_obj = BeautifulSoup(html.read(), "lxml")
        table = bs_obj.findAll("table")[0]
        #rows = table.findAll("tr")
        path = os.getcwd() + "/" + self.name + "_hero.csv"
        csvFile = open(path, "wt")
        writer = csv.writer(csvFile)
        try:
            for row in table.findAll("thead"):
                headRow = []
                for cell in row.findAll("th"):
                    headRow.append(cell.get_text())
                writer.writerow(headRow)
            for row in table.findAll("tr"):
                csvRow = []
                for cell in row.findAll("td"):
                    csvRow.append(cell.get_text().strip())
                writer.writerow(csvRow)
        finally:
            csvFile.close()

    def do_crawl_item(self, option):
        html = urlopen(self.link)
        bs_obj = BeautifulSoup(html.read(), "lxml")
        table = bs_obj.findAll("table")[0]
        path = os.getcwd() + "/" + self.name + "_" + option +".csv"
        csvFile = open(path, "wt")
        writer = csv.writer(csvFile)
        try:
            for row in table.findAll("thead"):
                headRow = []
                for cell in row.findAll("th"):
                    headRow.append(cell.get_text().strip())
                writer.writerow(headRow)
            for row in table.findAll("tr"):
                csvRow = []
                for cell in row.findAll("td"):
                    csvRow.append(cell.get_text())
                writer.writerow(csvRow)
        finally:
            csvFile.close()

    def do_crawl_match(self, match):
        pass

    '''
    def save_data(self, data):
        path = os.getcwd() + "/hero.csv"
        csvFile = open(path, "wt")
        writer = csv.writer(csvFile)
        try:
            for row in data:
                csvRow = []
                for cell in row.findAll(["td", "th"]):
                    csvRow.append(cell.get_text())
                writer.writerow(csvRow)
        finally:
            csvFile.close()
    '''