import urllib.request
from bs4 import BeautifulSoup
from myRetrieve import retrieve
import os
import time

class naverwebtoon:
    def __init__(self, main_url, sub_url, folder):
        self.user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'
        self.headers = {'User-Agent': self.user_agent}
        self.main_url = main_url
        self.sub_url = sub_url
        self.folder = folder

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
        for item in results:
            try:
                save_path = save_folder + str(i) + '.jpg'
                req = urllib.request.Request(item.get('src'), headers=self.headers)
                retrieve(req, save_path)
                i+=1
            except:
                pass


    def getLastPageIndex(self):
        url = self.main_url + str(10000)
        content = self.content(url)
        results = content.find("strong", class_="page")
        index = results.contents[0].text
        return int(index) + 1

    def download(self):
        page_ind = self.getLastPageIndex()  
        episode_ind = 1
        for i in reversed(range(1, page_ind)):
            page_url = self.main_url + str(i)
            episode_list = self.getEpisodeList(page_url)

            for url in episode_list:
                save_folder = self.folder + str(episode_ind) + '/'
                if not os.path.exists(save_folder):
                    os.mkdir(save_folder)
                
                episode_url = self.sub_url + url
                print("downloading episode", episode_ind)
                self.getImages(episode_url, save_folder)
            
                episode_ind += 1



if __name__ == '__main__':
    #main_url = r"https://comic.naver.com/webtoon/list.nhn?titleId=641253&weekday=fri&page="
    main_url = r"https://comic.naver.com/webtoon/list.nhn?titleId=699415&weekday=thu&page="
    sub_url = r"https://comic.naver.com/"
    #folder = "Lookism/"
    folder = "delete/"
    nw = naverwebtoon(main_url, sub_url, folder)
    nw.download()
