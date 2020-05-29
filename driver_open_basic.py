#coding: UTF-8
import time                            # スリープを使うために必要
from selenium import webdriver         # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary             # パスを通すためのコード

driver = webdriver.Chrome()            # Chromeを準備
driver.get('https://www.google.com/')  # Googleを開く
time.sleep(10)                          # 10秒間待機
driver.quit()                          # ブラウザを閉じる
