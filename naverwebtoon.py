import urllib.request
from bs4 import BeautifulSoup
from myRetrieve import retrieve
import os
import time
from Unbuffered import Unbuffered
import sys
sys.stdout = Unbuffered(sys.stdout)


class naverwebtoon:
    def __init__(self, main_url, sub_url, comic_list, folder):
        self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        self.headers = {'User-Agent': self.user_agent}
        self.main_url = main_url
        self.comic_url = "" # formulate from getComic
        self.sub_url = sub_url
        self.comic_list = comic_list
        self.folder = folder
        self.comic_folder = "" # formulate from getComic

    def content(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(req)
        time.sleep(1)
        page = response.read()
        content = BeautifulSoup(page, "html.parser")
        return content

    def getEpisodeList(self, url):
        content = self.content(url)
        results = content.find("div", class_="webtoon").find('table')
        list_ = []
        for item in results.find_all('td', class_='title'):
            link = item.find('a').get('href')
            list_.append(link) 
        
        return list(reversed(list_))

    def getImages(self, url, save_folder):
        content = self.content(url)
        results = content.find("div", class_="wt_viewer")
        i = 1
        for item in results.find_all('img'):
            save_path = save_folder + str(i) + '.jpg'
            if os.path.exists(save_path):
                i+=1
                continue
            req = urllib.request.Request(item.get('src'), headers=self.headers)
            retrieve(req, save_path)
            i+=1


    def getLastPageIndex(self):
        url = self.comic_url + str(10000)
        content = self.content(url)
        results = content.find("strong", class_="page")
        index = results.contents[0].text
        return int(index) + 1

    def getComic(self, comic):
        content = self.content(self.main_url)
        results = content.find("a", title=comic)
        if not results:
            return False
        self.comic_url = self.sub_url + results.get('href') + '&page='
        self.comic_folder = self.folder + comic + '/'
        if not os.path.exists(self.comic_folder):
            os.mkdir(self.comic_folder)
        print('retrieving comic', comic)
        return True

    def download(self):
        for comic in comic_list:
            if not self.getComic(comic):
                print("no comic", comic)
                continue

            page_ind = self.getLastPageIndex()  
            episode_ind = 1
            for i in reversed(range(1, page_ind)):
                page_url = self.comic_url + str(i)
                episode_list = self.getEpisodeList(page_url)

                for url in episode_list:
                    save_folder = self.comic_folder + str(episode_ind) + '/'
                    if not os.path.exists(save_folder):
                        os.mkdir(save_folder)
                    
                    episode_url = self.sub_url + url
                    print("downloading episode", episode_ind)
                    self.getImages(episode_url, save_folder)
                
                    episode_ind += 1



if __name__ == '__main__':
    
    main_url = r"https://comic.naver.com/webtoon/weekday.nhn"
    sub_url = r"https://comic.naver.com"
    comic_list = [r'신의 탑', r'윈든브레이커', r'니편내편', r'여신강림', r'랜덤체팅의 그녀', r'제로게임', r'연애혁명', r'외모지상주의', r'유미의 세포들', r'맘마미안']
    folder = 'comics/'
    nw = naverwebtoon(main_url, sub_url, comic_list, folder)
    nw.download()
