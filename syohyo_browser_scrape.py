#coding: UTF-8
from selenium import webdriver
import chromedriver_binary  # パスを通せる
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import pprint  # pprint.pprint()で出力が改行されて見やすくなる
import os # ディレクトリパス簡略化
import csv

# 便利関数
def print_html(x):
    print(bs4.BeautifulSoup(x.get_attribute('innerHTML'), 'html.parser').prettify())

seach_word = ""

browser = webdriver.Chrome()
# サイトに移動
URL = 'https://www.j-platpat.inpit.go.jp/s0100'
browser.get(URL)
# 商標を選択
radiobtn = browser.find_element_by_xpath("//*[@id='mat-radio-5']/label/div[1]")
radiobtn.click()

form_area = browser.find_element_by_tag_name('form') # 簡易検索エリア
form_text = form_area.find_element_by_name("s01_srchCondtn_txtSimpleSearch")
# ----------------------------------------------------------------
# csvファイル読み込み
# ----------------------------------------------------------------
df = pd.read_csv('trademark_names.csv', index_col=0) # index_col=0つけるとcsvの０列目をdfの０列目にしてくれる
print(df)
col_name = df.loc[:, 'name']    # 列を表示
print(col_name)
print(type(col_name))  # <class 'pandas.core.series.Series'>

for name in col_name:
    # print(type(name))  # -> <class 'str'>
    seach_word = name
    print('検索ワード：' + seach_word)

    form_text.clear() # 繰り返し検索時、すでに入っているキーワードは消す
    form_text.send_keys(seach_word)
    search_btn = form_area.find_element_by_name('s01_srchBtn_btnSearch')
    search_btn.click()
    time.sleep(2)
"""
    html = browser.find_element_by_id('s01_searchRslt')
    # soup = BeautifulSoup(html, "html.parser")
    soup = bs4.BeautifulSoup(html.get_attribute('innerHTML'), 'html.parser')

    # print(soup.table.tr) # -> 成功
    # rows = (soup.table.tr).text
    rows = soup.table.findAll("tr")  # まとめて入ってる

    # 追加書き込みモードで
    with open(f'{os.getcwd()}/syohyo.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td', 'th']):
                csvRow.append(cell.get_text().strip().replace(' ', ''))
            print(repr(csvRow))  # repr:空白文字などがわかりやすくなる
            writer.writerow(csvRow)
"""
browser.close()
