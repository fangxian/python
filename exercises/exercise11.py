#import io

def filt(x):
    f=open('/users/yufangxian/Documents/exercise/filter.txt','r')
    if x in f.read():
        print('Freedom')
    else:
        print('Human Rights')
    f.close()


if __name__=='__main__':
    while True:
        try:
            x=input("please input:")
            filt(x)
        except:
            print("input did not execute")
