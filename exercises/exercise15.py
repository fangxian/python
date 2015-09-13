from openpyxl import Workbook
import re

file=open('/users/yufangxian/Documents/exercise/numbers.txt','r')
f=file.read()
f_1=eval(f)
#print(f_1)
wb=Workbook(optimized_write=True)

ws=wb.create_sheet()

for irow in range(len(f_1)):
    ws.append( k for k in f_1[irow])
wb.save('/users/yufangxian/Documents/exercise/mm1.xlsx')
