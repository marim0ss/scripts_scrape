#coding: UTF-8
from selenium import webdriver
import chromedriver_binary  # パスを通せる
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import pprint  # pprint.pprint()で出力が改行されて見やすくなる

# 便利関数
def print_html(x):
    print(bs4.BeautifulSoup(x.get_attribute('innerHTML'), 'html.parser').prettify())

# ブラウザ起動
browser = webdriver.Chrome()

# サイトに移動
URL = 'https://www.google.com/search?source=hp&ei=wpDCXrvNLZmJoAS-oanIBQ&q=%E5%A4%A9%E6%B0%97%E4%BA%88%E5%A0%B1&oq=&gs_lcp=CgZwc3ktYWIQARgEMg4IABDqAhC0AhCaARDlAjIOCAAQ6gIQtAIQmgEQ5QIyDggAEOoCELQCEJoBEOUCMg4IABDqAhC0AhCaARDlAjIOCAAQ6gIQtAIQmgEQ5QIyDggAEOoCELQCEJoBEOUCUABYAGDwQ2gBcAB4AIABAIgBAJIBAJgBAKoBB2d3cy13aXqwAQY&sclient=psy-ab&ved=0ahUKEwi7tv6qxb3pAhWZBIgKHb5QClkQ4dUDCA0'
key_word = 'コナン'  # ブラウザにいれるので日本語で
browser.get(URL)

# 検索ワード入力欄でボタンをクリック
searchform = browser.find_element_by_id('searchform')
text = searchform.find_element_by_name("q") # 検索用テキストボックスの要素を取得
text.clear() # すでに入っているキーワードを消す
text.send_keys(key_word)
btn = searchform.find_element_by_tag_name('button')
btn.click()
time.sleep(3)

# クリック後
stats = browser.find_element_by_id("result-stats").text
print(stats)
print(type(stats))  # -> <class 'str'>

result = re.search(r'約\s(.+)\s件', stats) # -> <class 'str'>
print(result[1])
browser.close()
