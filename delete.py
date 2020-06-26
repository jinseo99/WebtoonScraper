import urllib.request
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {'User-Agent': user_agent}

url = "https://comic.naver.com/webtoon/list.nhn?titleId=641253&weekday=fri&page=10000"
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
page = response.read()
content = BeautifulSoup(page, "html.parser")
results = content.find("strong", class_="page")
index = results.contents[0].text

print(index)

print("welcome")