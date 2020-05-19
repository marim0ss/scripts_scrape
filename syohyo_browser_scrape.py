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
URL = 'https://www.j-platpat.inpit.go.jp/s0100'
browser.get(URL)
# ラジオボタン商標を選択
radiobtn = browser.find_element_by_xpath("//*[@id='mat-radio-5']/label/div[1]")
radiobtn.click()

time.sleep(3)

browser.close()
