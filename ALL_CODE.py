#KOSPY_CODE : 코스피코드 목록 배열
#KOSDAQ_CODE : 코스닥코드 목록 배열
#ALL_CODE : 모든 종목 코드 배열

import requests
from bs4 import BeautifulSoup
import re

KOSPY_url = "http://finance.daum.net/quote/all.daum?type=S&stype=P"
KOSDAQ_url = "http://finance.daum.net/quote/all.daum?type=S&stype=Q"
KOSPY_html = requests.get(KOSPY_url).text
KOSDAQ_html =  requests.get(KOSDAQ_url).text

KOSPY_soup = BeautifulSoup(KOSPY_html, "html.parser")
KOSDAQ_soup = BeautifulSoup(KOSDAQ_html, "html.parser")
KOSPY_list = KOSPY_soup.select('td a')
KOSDAQ_list = KOSDAQ_soup.select('td a')

#  종목 Code 배열로 저장 & a href내의 숫자 추출  기능
KOSPY_CODE = []
KOSDAQ_CODE = []
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


ALL_CODE = KOSPY_CODE + KOSDAQ_CODE



#다음 증권에서 종목코드가 6자리가 아닌 종목들 제거
del_list_index = []
for i in range(len(ALL_CODE)):
    if (len(ALL_CODE[i]) != 6):
        del_list_index.append(i)

index=0
for i in del_list_index:
    del ALL_CODE[i-index]
    index += 1

# 시세 차트가 없는 페이지 종목들 제거
del ALL_CODE[174]
del ALL_CODE[334]


#MAIN
if __name__ == "__main__":
    print(KOSPY_CODE)
    print("ppppppppppppppppppppppppp", len(KOSPY_CODE))

    print(KOSDAQ_CODE)
    print("qqqqqqqqqqqqqqqqqqqqqq", len(KOSDAQ_CODE))
    print(ALL_CODE)
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaa", len(ALL_CODE))
