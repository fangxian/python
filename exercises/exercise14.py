from openpyxl import Workbook
import re
#from openpyxl.compat import range
#from openpyxl.cell import get_row_letter
file=open('/users/yufangxian/Documents/exercise/student.txt','r')
f=file.read()
x=re.sub('\n','',f)
x_1=re.sub('\t','',x)
x_2=eval(x_1)
#print(x_1)
#x_4=dict(x_3)
#print(x_2)
x_3=dict(x_2)
print(x_3['1'][1])

wb=Workbook(optimized_write=True)

ws=wb.create_sheet()

for irow in range(len(x_3)):
    #x_3['%s' %(irow+1)].insert(0,'%s' %(irow+1))
    x_4=list('%s' %(irow+1))+x_3['%s' %(irow+1)]
    #ws.append(['%s' % k for k in x_3['%s' %(irow+1)] ])
    ws.append(['%s' % k for k in x_4])
wb.save('/users/yufangxian/Documents/mm.xlsx')

