import urllib.request
import bs4

url = "http://finance.daum.net/item/chart.daum?code=035720"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

top_right = bsObj.find("em", {"class":"curPrice keep"})
#first_a = top_right.find("h2")
#Intt=top_right.text
#int(Intt)


test = (top_right.text).replace(",", "")

print(int(test))


# 가격 데이터 (ex:150,000) -> Text -> relplace로 , 제거  -> 숫자로