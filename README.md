# WebtoonScraper

WebtoonScraper allows scraping of images in webtoons.

## Usage

detailed usage in naverwebtoon.py

```python
  main_url = r"https://comic.naver.com/webtoon/weekday.nhn"
  sub_url = r"https://comic.naver.com"
  #comic_list = [r'신의 탑', r'윈드브레이커', r'니편내편', r'여신강림', r'랜덤채팅의 그녀!', r'제로게임', r'갓물주', r'연애혁명', r'외모지상주의', r'유미의 세포들', r'맘마미안']
  comic_list = [r'랜덤채팅의 그녀!', r'갓물주'] # choose your comic titles from https://comic.naver.com
  folder = 'comics/' # saving directory
  nw = naverwebtoon(main_url, sub_url, comic_list, folder)
  nw.download()
```
