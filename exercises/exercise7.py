import glob
import re
words_dict={}

def count_string(file):
    count=0
    f=open(file,'r')
    for line in f:
        match=re.findall(r'[a-zA-Z]+',line)
        for i in match:
            if i not in words_dict:
                words_dict[i]=1
            else:
                words_dict[i]+=1
    for v,k in words_dict.items():
        if k>=count:
            count=k
    for v,k in words_dict.items():
        if k==count:
            print(v,k)
for file in glob.glob('/users/yufangxian/Documents/exercise/text/*.txt'):
    count_string(file)
