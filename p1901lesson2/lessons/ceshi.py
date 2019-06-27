import requests
import bs4
r = requests.get('http://10.2.0.193:8000/exercises/spider/level2/')


print(r.text)

