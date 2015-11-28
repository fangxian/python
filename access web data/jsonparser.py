from urllib import request
import json

url = request.urlopen('http://python-data.dr-chuck.net/comments_205542.json')
data = url.read().decode("utf-8")
#print(data)
#print(data.decode("utf-8"))
info =json.loads(data)
s=0
count=0

for i in range(len(info['comments'])):
	s+=info['comments'][i]['count']

print(s)
