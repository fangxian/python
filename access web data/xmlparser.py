from urllib import request
from lxml import etree

url = request.urlopen('http://python-data.dr-chuck.net/comments_205538.xml')
data = url.read()
lat=[]
s=0
tree = etree.fromstring(data)
results = tree.findall('comments')
print(results)
for i in range(len(results)):
	lat.append(results[i].find('comment').find('count').text)
	
print(lat)
	#print(lat)
#print(results)