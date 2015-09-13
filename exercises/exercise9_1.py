from bs4 import BeautifulSoup
import io
file = io.open('/users/yufangxian/Documents/test.html', 'r')
soup = BeautifulSoup(file,'html.parser')
print(soup.getText().strip("\n"))


file.close()
