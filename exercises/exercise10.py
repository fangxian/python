from  urllib import request
from bs4 import BeautifulSoup
import re

def show_url(url):
    content=request.urlopen(url).read()
    soup=BeautifulSoup(content,'html.parser')
    for link in soup.findAll('a'):
        print(link.get('href'))
    
        #print(tag['meta'])



if __name__=='__main__':
    show_url('https://www.python.org/events/python-events/')
