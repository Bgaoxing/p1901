#ip : 10.2.5.71
#账户 student 密码 student
import requests
from bs4 import BeautifulSoup
# res = requests.get(url="http://blog.jobbole.com/114694/")
# soup = BeautifulSoup(res.text)
# print('文章标题{}'.format(soup.select('div.entry-header h1')[0].text))
#
# a_lists = soup.select('li span.digg-item-updated-title a')
# for a in a_lists:
#     href = a.attrs['href']
#     res = requests.get(url=href)
#     soup = BeautifulSoup(res.text)
#     print('文章标题{}'.format(soup.select('div.entry-header h1')[0].text))
crawled_list = list()
def start(url):
    if url in crawled_list:
        return
    res = get(url)
    print('文章标题{}'.format(res.select('div.entry-header h1')[0].text))

    a_lists = res.select('li span.digg-item-updated-title a')
    for a in a_lists:
        href = a.attrs['href']
        run(href)


def run(href):
    if href in crawled_list:
        return
    res = get(href)
    print('文章标题{}'.format(res.select('div.entry-header h1')[0].text))

    a_lists = res.select('li span.digg-item-updated-title a')
    for a in a_lists:
        href = a.attrs['href']
        run(href)

def get(url):
    """
    这个函数专门是爬去页面,并且把页面的信息转化成dom返回
    :param url:
    :return:
    """
    crawled_list.append(url)
    import time
    time.sleep(2)
    print('---------------')
    print(crawled_list)
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text)
    return soup

if __name__ == "__main__":
    start("http://blog.jobbole.com/114694/")
