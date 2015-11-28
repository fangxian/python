import re
from urllib import request
from bs4 import BeautifulSoup
import json

i=1
count = 0
def search(url1):
	url_s = request.urlopen(url1)
	soup = BeautifulSoup(url_s,'lxml')
	tags = soup('a')
	return tags

url='https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Samy.html '

while True:
	for tag in search(url):
		if i==18:
			print(tag)
			#print(tag.get('href',None))
			url=tag.get('href',None)
			i=1
			break
			#print(tags)
		#print(tag)
			
		else:
			i+=1
	count +=1
	if count ==7:
		break