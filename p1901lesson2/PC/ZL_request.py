import json
import re
import requests
from requests import RequestException


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page(html):
    pattern = re.compile('<div.*?list-item.*?data-title="(.*?)".*?data-score="(.*?)".*?>.*?<img.*?src="(.*?)".*?/>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'title': item[0],
            'score': item[1],
            'image': item[2],
        }


def write_to_file(content):
    with open('gangwei.txt', 'a', encoding='utf-8')as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False))


def main():
    url = "https://sou.zhaopin.com/?jl=801&we=0001&kw=python&kt=3&sf=0&st=0"
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main()
