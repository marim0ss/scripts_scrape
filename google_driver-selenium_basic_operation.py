#coding: UTF-8
from selenium import webdriver
import chromedriver_binary  # パスを通せる
import bs4
import pandas as pd
import time

myword = "crossfor"
# 便利関数
def print_html(x):
    print(bs4.BeautifulSoup(x.get_attribute('innerHTML')).prettify())

# ブラウザ起動
browser = webdriver.Chrome()

# googleサイトに移動
URL = 'https://www.google.jp'
browser.get(URL)

text = browser.find_element_by_name("q") # ID属性ないのでnameから検索用テキストボックスの要素を取得し
text.send_keys(myword) # 文字列をテキストボックスに入力
time.sleep(5)          # 入力されきるまでにラグがあるのでちょっと待つ
btn = browser.find_element_by_name("btnK") # 検索用ボタンにはID属性がないのでname属性から取得し
btn.click()            # 対象をクリック！
time.sleep(3)          # 確認タイム
browser.quit()         # 閉じないと残っちゃう
