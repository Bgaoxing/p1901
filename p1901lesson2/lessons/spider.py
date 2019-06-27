# 作用于动态页面的爬取，用js渲染的页面
from telnetlib import EC
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

#  不弹出浏览器
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path="/Users/rimi/Desktop/chromedriver",
                          options=options)

# driver = webdriver.Chrome(executable_path="/Users/rimi/Desktop/chromedriver")
driver.get("https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0")
# time.sleep(1)

try:
    # 等待期待的条件发生
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.TAG_NAME, 'tr')))

except Exception as e:
    print(e)

# time.sleep(5)
# search_tag = driver.find_element_by_name('search_text')
# search_tag.send_keys('范冰冰')
# search_tag.submit()
# time.sleep(30)

tag = driver.find_element_by_class_name("list")
assert isinstance(tag, WebElement)

# tag = driver.find_element_by_id("userinfo")
# for t in tag.find_elements_by_tag_name('tr'):
#     user_info = t.find_elements_by_tag_name("td")
#     username = user_info[0].text
#     age = user_info[1].text
#     gender = user_info[2].text
#    print(username, age, gender)

for t in tag.find_elements_by_class_name('item'):
    title = t.find_element_by_tag_name('p')
    score = t.find_element_by_tag_name('strong')
    print(title.text, score.text)

# print(type(tag))

# print(driver.title)
# time.sleep(10)
driver.quit()