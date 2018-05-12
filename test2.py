import requests
from bs4 import BeautifulSoup

url = "http://m.finance.daum.net/m/item/item_daily.daum?code=035720&page=2"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

for tag in soup.select('tbody td.idx'):
    tag.replace("," , "")
    print(tag.text)
