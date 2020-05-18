#coding: UTF-8
from selenium import webdriver
import chromedriver_binary  # パスを通せる
import bs4
import pandas as pd
import time
import pprint  # pprint.pprint()で出力が改行されて見やすくなる

# 便利関数
def print_html(x):
    print(bs4.BeautifulSoup(x.get_attribute('innerHTML'), 'html.parser').prettify())

# ブラウザ起動
browser = webdriver.Chrome()

# サイトに移動
URL = 'https://www.google.com/search?q=%E3%82%B3%E3%83%8A%E3%83%B3&oq=%E3%82%B3%E3%83%8A%E3%83%B3&aqs=chrome..69i57j0l2j69i65l3j69i61l2.1724j0j7&sourceid=chrome&ie=UTF-8'
browser.get(URL)

# 検索ワード入力欄でボタンをクリック
searchform = browser.find_element_by_id('searchform')
btn = searchform.find_element_by_tag_name('button')
btn.click()
time.sleep(3)

html = browser.find_element_by_id('main')  # これが動的に生成されたHTML
# print_html(html)

result = html.find_element_by_id('result-stats')
print_html(result)
print(type(result))
browser.close()
