import urllib.request
import bs4

url = "http://finance.daum.net/item/main.daum?code=035720"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

top_right = bsObj.find("em", {"class":"curPrice up"})
#first_a = top_right.find("h2")
#Intt=top_right.text
#int(Intt)

def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

test = (top_right.text).replace(",","")

print(int(test))