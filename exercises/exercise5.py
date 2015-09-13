f=open('/users/yufangxian/Documents/exercise/exercise1.py','r')
char=f.read(1)
count=0
while char:
    if char==' ':
        count+=1
    char=f.read(1)
print(count)
