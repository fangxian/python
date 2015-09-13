import glob
import re

def count_file(file):
    blankcount=0
    charcount=0
    linecount=0
    wordscount=0
    f=open(file,'r')
    for line in f:
        if line.startswith('\n'):
            blankcount+=1
        else:
            linecount+=1
        charcount+=len(line)
        match=re.findall(r'[a-zA-Z]+',line)
        wordscount+=len(match)
    print('the number of blankcount is:',blankcount)
    print('the number of charcount is:',charcount)
    print('the number of wordscount is:',wordscount)
    print('the number of linecount is:',linecount)
    print(file)
    f.close()
for file in glob.glob('/users/yufangxian/Documents/exercise/*.py'):
    count_file(file)
