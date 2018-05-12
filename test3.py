import requests
from bs4 import BeautifulSoup

url = "http://m.finance.daum.net/m/item/item_daily.daum?code=035720&page=2"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
test = soup.select('tbody td.idx')
print((test[4]))
print(type(test))
array = [test[i].text for i in range (len(test))]


print (array)

for i in range(len(array)):
    array[i] =array[i].replace(",","")



print(array[1], "d")

# 데이터 받아서 배열에 집어넣기 기능