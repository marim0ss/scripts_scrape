#coding: UTF-8
from selenium import webdriver
import chromedriver_binary  # パスを通せる
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
import pprint  # pprint.pprint()で出力が改行されて見やすくなる
import os # ディレクトリパス簡略化
import csv

# 便利関数-------
def print_html(x):
    print(bs4.BeautifulSoup(x.get_attribute('innerHTML'), 'html.parser').prettify())

URL = 'https://www.j-platpat.inpit.go.jp/s0100'
seach_word = ""
# ----------------------------------------------------------------
# datetimeオブジェクトを、任意の書式で文字列に変換
# ----------------------------------------------------------------
date = datetime.date.today()
f = '%Y-%m-%d'
date_today = date.strftime(f)
# print(date_today)

browser = webdriver.Chrome()
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
# print(type(col_name))  # <class 'pandas.core.series.Series'>

for name in col_name:
    # print(type(name))  # -> <class 'str'>
    seach_word = name
    print('検索ワード：' + seach_word)

    form_text.clear() # 繰り返し検索時、すでに入っているキーワードは消す
    form_text.send_keys(seach_word)
    search_btn = form_area.find_element_by_name('s01_srchBtn_btnSearch')
    search_btn.click()
    time.sleep(3)

    search_result_area = browser.find_element_by_id('s01_searchRslt')    # 検索結果一覧のエリア
    soup = bs4.BeautifulSoup(search_result_area.get_attribute('innerHTML'), 'html.parser')
    try:
        rows = soup.tbody.findAll("tr")  # まとめて入ってる
        # pprint.pprint(rows)  # Ok

        # 追加書き込みモードにする a
        with open(f'{os.getcwd()}/syohyo.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            for row in rows:
                csvRow = []
                for cell in row.findAll(['td', 'th']):
                    # print(repr(cell.img))
                    cell_text = cell.get_text()
                    if cell.img: cell_text = '-'
                    csvRow.append(cell_text.strip().replace(' ', ''))
                csvRow.extend((date_today, seach_word))   # できた１列にデータ作成日と元の検索ワードを追加
                print(repr(csvRow))  # repr:空白文字などがわかりやすくなる
                writer.writerow(csvRow)
    except:
        print(seach_word + ' は検索結果が０件です')
        continue
browser.close()
