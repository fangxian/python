__author__ = 'yufangxian'


from bs4 import BeautifulSoup
from urllib import request
import numpy as np
import pandas as pd
import os
from multiprocessing import Pool, Process
import time



class Dota2_crawler(object):
    def __init__(self):
        self._base_url = r"http://www.gosugamers.net/dota2/gosubet?r-page="

    def crawler_page(self):
        start_time = time.time()
        for i in range(1, 50):
            url = self._base_url + str(i)
            self.do_crawler(url)
        print("time consume: %s" % (time.time() - start_time))

    def do_crawler(self, url):
        parsed_url = request.urlopen(url)
        soup = BeautifulSoup(parsed_url, 'lxml')
        soup_lose = soup.findAll('span', class_="score losser hscore")
        soup_win = soup.findAll('span', class_="score winner ascore")
        soup_team1 = soup.findAll('span', class_="opp opp1")
        soup_team2 = soup.findAll('span', class_="opp opp2")
        soup_result = soup.findAll('span', class_="hidden")
        path = '/users/yufangxian/Documents/dota_result'
        '''
        p1 = Process(target=self.save_team1, args=(path, soup_team1,))
        p1.start()
        p2 = Process(target=self.save_team2, args=(path, soup_team2,))
        p2.start()
        p3 = Process(target=self.save_res, args=(path, soup_result,))
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        '''

        self.save_team1(path, soup_team1)
        self.save_team2(path, soup_team2)
        self.save_res(path, soup_result)
        #print("all processes have done!")
        #self.save_res(path, soup_lose, soup_win, soup_team1, soup_team2, soup_result)

    @staticmethod
    def save_team1(path, soup_team1):
        saving_team1 = path + '/dota2_team1.txt'
        for item in soup_team1[-25:]:
            s = str(item.get_text())
            with open(saving_team1, 'a') as fp2:
                fp2.write(s[:-2]+'\n')

    @staticmethod
    def save_team2(path, soup_team2):
        saving_team2 = path + '/dota2_team2.txt'
        for item in soup_team2[-25:]:
            with open(saving_team2, 'a') as fp3:
                fp3.write(str(item.get_text())+'\n')

    @staticmethod
    def save_res(path, soup_result):
        #saving_loss_path = path + '/dota2_loss.txt'
        #saving_win_path = path +'/dota2_win.txt'
        #saving_team1 = path + '/dota2_team1.txt'
        #saving_team2 = path + '/dota2_team2.txt'
        saving_result = path + '/dota2_result.txt'
        '''
        for item in soup_lose:
            with open(saving_loss_path, 'a') as fp:
                fp.write(str(item.get_text())+'\n')

        for item in soup_win:
            with open(saving_win_path, 'a') as fp1:
                fp1.write(str(item.get_text())+'\n')
        '''

        for item in soup_result:
            with open(saving_result, 'a') as fp4:
                fp4.write(str(item.get_text())+'\n')


def merge_data():
    path = '/users/yufangxian/Documents/dota_result/'
    team1 = pd.read_table(path + 'dota2_team1.txt', header=None)
    team2 = pd.read_table(path + 'dota2_team2.txt', header=None)
    result = pd.read_table(path + 'dota2_result.txt', header=None)
    live_up = len(team1) -len(result) #caculate the upcoming and living matches
    add_0 = np.zeros(live_up)
    df = pd.DataFrame(add_0)
    final_result = df.append(result, ignore_index=True)
    final_table = pd.concat([team1, final_result], axis=1, join_axes=[team1.index])
    final_table = pd.concat([final_table, team2], axis=1, join_axes=[final_table.index])
    final_table.to_csv(path+'final_result.csv')


def mining_data():
    pass





def main():
    dota2 = Dota2_crawler()
    dota2.crawler_page()
    merge_data()

if __name__ == '__main__':
    main()
