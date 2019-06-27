import requests
import bs4
import threading

urls = ["http://www.xiaohuar.com/list-1-0.html"]
images_store = "./images"


def download_image(url):
    import os
    print("Downloading {}".format(url))
    # 使用WGET命令下载图片
    os.system("cd {} && wget '{}'".format(images_store, url))


page_index = 0
while True:
    # 如果请求完所有的URL则退出。
    if page_index >= len(urls):
        break

    # 爬取新的URL地址
    url = urls[page_index]

    response = requests.get(url)
    if response.status_code != 200:
        page_index += 1
        continue

    # 解析页面所有的图片地址。
    bs = bs4.BeautifulSoup(response.text)
    items_div = bs.find("div", attrs={"class": "item_list infinite_scroll"})
    img_urls = []
    for img in items_div.find_all("div", attrs={
        "class": "item_t"}, recursive=True):
        pic_info = img.find("img")
        img_url = "http://www.xiaohuar.com" + pic_info.attrs["src"]
        # 采用多线程方式下载图片
        threading.Thread(target=download_image, args=(img_url,), daemon=True).start()

    # 找到所有的页面并添加的爬去队列。
    pages = bs.find("div", attrs={"class": "page_num"})
    for page in pages.find_all("a", recursive=True):
        if "href" in page.attrs:
            url = page.attrs["href"]
            if url not in urls:
                urls.append(url)

    page_index += 1
