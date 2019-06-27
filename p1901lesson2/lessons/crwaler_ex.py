from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup
class Crwaler:

    def __init__(self,url):
        self.queue = Queue(maxsize=10000)
        self.crwaled_list = list()
        self.pools = ThreadPoolExecutor(max_workers=10)
        self.init_url = url

    def start(self,url):
        self.queue.put(url)

    def worker(self):
        while True:
            print('17--------')

            task_url = self.queue.get()
            try:
                res = requests.get(url=task_url)
                self.handler(res.text)
            except Exception:
                pass

    def handler(self,text):
        soup = BeautifulSoup(text)
        a_lists = soup.select('li span.digg-item-updated-title a')
        print('文章标题{}'.format(soup.select('div.entry-header h1')[0].text))
        for a in a_lists:
            href = a.attrs['href']
            if href in self.crwaled_list:
                continue
            self.crwaled_list.append(href)
            self.queue.put(href)

    def run_server(self):
        self.pools.submit(self.worker)
        self.start(self.init_url)


crwaler = Crwaler(url="http://blog.jobbole.com/114694/")

crwaler.run_server()