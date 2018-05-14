# 데이터 받아서 배열에 집어넣기 기능
# MAL_Function(x)
# Now_Price_Function(x)
# MAL_Line(x)
# def err_MAL_Line(x)
# err_MAL_Line(x)
import ALL_CODE
import requests
from bs4 import BeautifulSoup


# 현재 가격 함수 / 입력값 : 종목코드값
# 배열로 저장된 종목 코드 하나를 주소 Code에 대입하여 현재 가격 출력
def Now_Price_Function(x):
    url_test = "http://m.finance.daum.net/m/item/main.daum?code={0}".format(x)
    input_html = requests.get(url_test).text
    input_soup = BeautifulSoup(input_html, "html.parser")
    Now_Price = input_soup.find("span", {"class":"price"})
    Now_Price = Now_Price.text.replace(",", "")
    return int(Now_Price)

print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

#현재가격 배열 생성 함수
def Now_Price_Arr_F(x):
    url_test = "http://m.finance.daum.net/m/item/main.daum?code={0}".format(x)
    input_html = requests.get(url_test).text
    input_soup = BeautifulSoup(input_html, "html.parser")
    Now_Price = input_soup.find("span", {"class":"price"})
    Now_Price = Now_Price.text.replace(",", "")
    return int(Now_Price)


if __name__ == "__main__":
    print("TEST ")
    print(Now_Price_Function(ALL_CODE.ALL_CODE[0])) #int
    print(type(Now_Price_Function(ALL_CODE.ALL_CODE[0])))  #int
    print(type(ALL_CODE.ALL_CODE[0]))  #str
    print(Now_Price_Function(ALL_CODE.ALL_CODE[0])==6140)

### 예외 코드들 제외한 코드배열 받아서 for문 돌리기
    n_array = []
    for i in range(len(ALL_CODE.ALL_CODE)):
        n_array.append(Now_Price_Function(ALL_CODE.ALL_CODE[i]))
        print(i, n_array[i])

