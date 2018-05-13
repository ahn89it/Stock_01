# 데이터 받아서 배열에 집어넣기 기능
import requests
from bs4 import BeautifulSoup

url1 = "http://m.finance.daum.net/m/item/item_daily.daum?code=035720"+"&page=1"
html1 = requests.get(url1).text
soup1 = BeautifulSoup(html1, "html.parser")
test1 = soup1.select('tbody td.idx')
array1 = [test1[i].text for i in range (len(test1))]
print (array1)
for i in range(len(array1)):
    array1[i] =array1[i].replace(",","")
print(array1[1])



url2 = "http://m.finance.daum.net/m/item/item_daily.daum?code=035720"+"&page=2"
html2 = requests.get(url2).text
soup2 = BeautifulSoup(html2, "html.parser")
test2 = soup2.select('tbody td.idx')
array2 = [test2[i].text for i in range (len(test2))]
print (array2)
for i in range(len(array2)):
    array2[i] =array2[i].replace(",","")
print(array2[1])

