import random
import string
import sqlite3
def gene():
    str=''
    for i in range(20):
        str+=chr(random.randint(30,100))

    return str

#x=gene()
#print(x)
        
#salt=''.join(random.sample(string.ascii_letters+string.digits,20))
#print(salt)

conn=sqlite3.connect('/users/yufangxian/Documents/exercise/test.db')
cursor=conn.cursor()
cursor.execute('create table user(id int ,name varchar(25))')

for i in range(1,21):
    salt=''.join(random.sample(string.ascii_letters+string.digits,20))
    cursor.execute("insert into user values('%d','%s')" %(i,salt))

cursor.close()
conn.commit()
conn.close()
