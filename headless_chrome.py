"""
# 未検証 ページのPDFは停止される恐れも。画像→PDF変換とかの方がいい？
#coding: UTF-8
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys

options = ChromeOptions()
# ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）。
options.add_argument('--headless')
# ChromeのWebDriverオブジェクトを作成する。
driver = Chrome(options=options)

# Googleのトップ画面を開く。
driver.get('https://www.google.co.jp/')

# タイトルに'Google'が含まれていることを確認する。
assert 'Google' in driver.title

# 検索語を入力して送信する。
input_element = driver.find_element_by_name('q')
input_element.send_keys('Python')
input_element.send_keys(Keys.RETURN)

# タイトルに'Python'が含まれていることを確認する。
assert 'Python' in driver.title

# スクリーンショットを撮る。
driver.save_screenshot('chrome_search_results.png')

# 検索結果を表示する。
for a in driver.find_elements_by_css_selector('h3 > a'):
    print(a.text)
    print(a.get_attribute('href'))

driver.quit()  # ブラウザーを終了する。
# https://qiita.com/orangain/items/6a166a65f5546df72a9d
# https://qiita.com/memakura/items/f80d2e2c59514cfc14c9
"""
