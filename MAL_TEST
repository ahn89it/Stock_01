# 데이터 받아서 배열에 집어넣기 기능
# MAL_Function(x)
# Now_Price_Function(x)
# MAL_Line(x)
# def err_MAL_Line(x)
# err_MAL_Line(x)
import ALL_CODE
import requests
from bs4 import BeautifulSoup


# X페이지 10개의 종가들 배열에 Input 함수
# 입력값은 X페이지 / 결과값은 X페이지의 종가들 배열 생성
def MAL_Function(x):
    url = "http://m.finance.daum.net/m/item/item_daily.daum?code=035720&page={0}".format(x)
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    test = soup.select('tbody td.idx')
    array = [test[i].text for i in range(len(test))]

    for i in range(len(array)):
        array[i] = int(array[i].replace(",", ""))

    return array


#종가 20개 모음 배열
End_Price = MAL_Function(1) + MAL_Function(2)

# 현재 가격 함수 / 입력값 : 종목코드값
# 배열로 저장된 종목 코드 하나를 주소 Code에 대입하여 현재 가격 출력
def Now_Price_Function(x):
    url_test = "http://m.finance.daum.net/m/item/main.daum?code={0}".format(x)
    input_html = requests.get(url_test).text
    input_soup = BeautifulSoup(input_html, "html.parser")
    Now_Price = input_soup.find("span", {"class":"price"}) #클래스 네임으로 현재가격 찾기
    Now_Price = int(Now_Price.text.replace(",", "")) #text str형으로 변환후 , 제거 후 int형으로 변환
    return  Now_Price

#현재가 계산
Now_Price = Now_Price_Function("035720")

# X일 이동평균값 함수
# (2일~X일 종가 모음) + 현재가격
def MAL_Line(x):
    sum = 0
    for i in range(1, x):
        sum = sum + End_Price[i]

    sum_x = sum + Now_Price
    MAL_Line_x = sum_x/x
    return MAL_Line_x



# 20일 이동평균값 (2일~20일 종가 모음) + 현재가격    *******다음 페이지 오류된 페이지 반영
# Page1의 마지막 종가와 Page2의 첫번째 종가가 겹침 따라서 Page3의 첫번째 종가 합산
def err_MAL_Line(x):
    sum = 0
    for i in range(1, x):
        sum = sum + End_Price[i]

    sum_x = sum + Now_Price - MAL_Function(2)[0] + MAL_Function(3)[0]
    MAL_Line_x = sum_x/x
    return MAL_Line_x



if __name__ == "__main__":
    print("TEST ")
    print("현재가", Now_Price)
    print("5일이동평균값", MAL_Line(5))
    print("20일이동평균값", err_MAL_Line(20))
