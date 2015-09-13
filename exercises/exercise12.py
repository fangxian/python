import sys

def filter_replace(x):
    f=open('/users/yufangxian/Documents/exercise/filter.txt','r')
    words=f.read()
    wordlist=words.split()
    #print(words)
    for word in wordlist:
        if word in x:
            x=x.replace(word,'**')
    print(x)





if __name__=='__main__':
    while True:
        x=input('please input:')
        filter_replace(x)
