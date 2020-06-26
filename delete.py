import urllib.request
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
headers = {'User-Agent': user_agent}

main_url = r"https://comic.naver.com/webtoon/weekday.nhn"
url = "https://comic.naver.com/webtoon/detail.nhn?titleId=183559&no=3&weekday=mon"
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
page = response.read()
content = BeautifulSoup(page, "html.parser")
results = content.find("div", class_="wt_viewer")
for item in results.find_all('img'):
    print(item)
#print(results.get('href'))