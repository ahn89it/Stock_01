import requests
from bs4 import BeautifulSoup
import re

url = "http://finance.daum.net/quote/all.daum?type=S&stype=P"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
test = soup.select('td a')


#  종목 Code 배열로 저장 & a href내의 숫자 추출  기능
array = []
for tag in test:
    link = tag['href']
    matched = re.search(r'\d+', link)
    code = matched.group(0)
    array.append(code)

print(array)
print(array[3], type(array[3]))

# 배열로 저장된 종목 코드 하나를 주소 Code에 대입하여 현재 가격 출력

input = array[1]
url_test ="http://m.finance.daum.net/m/item/main.daum?code=" + input
print(url_test)

input_html = requests.get(url_test).text
input_soup = BeautifulSoup(input_html, "html.parser")
result = input_soup.find("span", {"class":"price"}) #클래스 네임으로 현재가격 찾기
result = int(result.text.replace(",", "")) #text str형으로 변환후 , 제거 후 int형으로 변환
print(result, type(result))
