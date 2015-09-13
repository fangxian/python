from bs4 import BeautifulSoup
from urllib import request
from PIL import ImageFile
import os
#from StringIO import StringIO

def save_img(url,i):
    filename='abc'+str(i)+'.jpg'
    filepath=os.path.join('/users/yufangxian/Documents/exercise/picture',filename)
    image=open(filepath,'wb')
    image.write(url)
    image.close

def grab_picture(url):
    #p=ImageFile.Parser()
    content=request.urlopen(url).read()
    soup=BeautifulSoup(content,'html.parser')
    #print('hello')
    index=0
    for pict in soup.findAll('img'):
        print(pict.get('src'))
        #p.feed(pict.get('src'))
        #im=p.close()
        #im.save('/users/yufangxian/Documents/test.jpg')
        #filename='123'+'.jpg'
        #filepath=os.path.join('/users/yufangxian/Documents/exercise/picture',filename)
        data=request.urlopen(pict.get('src')).read()
        save_img(data,index)
        index+=1
        #image=open(filepath,'wb')
        #image.write(data)
        #image.close()
if __name__=='__main__':
    grab_picture('http://tieba.baidu.com/p/2166231880')
    #print(121212)
