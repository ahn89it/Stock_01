import requests
from bs4 import BeautifulSoup
import re

KOSPY_url = "http://finance.daum.net/quote/all.daum?type=S&stype=P"
KOSDAQ_url = "http://finance.daum.net/quote/all.daum?type=U&stype=Q"
KOSPY_html = requests.get(KOSPY_url).text
KOSDAQ_html =  requests.get(KOSDAQ_url).text

KOSPY_soup = BeautifulSoup(KOSPY_html, "html.parser")
KOSDAQ_soup = BeautifulSoup(KOSDAQ_html, "html.parser")
KOSPY_list = KOSPY_soup.select('td a')
KOSDAQ_list = KOSDAQ_soup.select('td a')

#  종목 Code 배열로 저장 & a href내의 숫자 추출  기능
KOSPY_CODE = [] #코스피코드 목록 배열
KOSDAQ_CODE = [] #코스닥코드 목록 배열
for tag in KOSPY_list:
    link = tag['href']
    matched = re.search(r'\d+', link)
    code = matched.group(0)
    KOSPY_CODE.append(code)

for tag in KOSDAQ_list:
    link = tag['href']
    matched = re.search(r'\d+', link)
    code = matched.group(0)
    KOSDAQ_CODE.append(code)

print(KOSPY_CODE)
print(len(KOSPY_CODE))

print(KOSDAQ_CODE)
print(len(KOSDAQ_CODE))

ALL_CODE = KOSPY_CODE + KOSDAQ_CODE
print(ALL_CODE)
print(len(ALL_CODE))


