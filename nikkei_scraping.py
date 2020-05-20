#coding: UTF-8
from selenium import webdriver
import chromedriver_binary  # パスを通せる
import bs4
import pandas as pd
import time

sample_word = 'サンプル'
nikkei_word = '((細彩 AND (行政指導 OR MDA OR 悪徳商法 OR キャッチセールス OR マルチ商法 OR ねずみ講OR 検挙 OR 送検 OR 捜査 OR 家宅捜索 OR 指名手配 OR 逮捕 OR 摘発 OR 犯罪 OR いたずら電話 OR インサイダー取引 OR 横領 OR 汚職 OR 贈収賄 OR 収賄 OR 贈賄 OR わいろ OR 架空取引 OR 株価操作 OR カラ出張 OR 監禁 OR 機密漏えい OR 脅迫 OR 恐喝 OR 金融犯罪 OR 架空請求 OR スキミング OR詐欺 OR ヤミ金融 OR 偽造 OR 偽札 OR 業務上過失致死傷 OR 業務上過失傷害 OR 業務上過失致死 OR 公務執行妨害 OR コンピューター犯罪 OR サイバーテロ OR ハッカー OR 不正アクセス OR 強盗 OR 殺人 OR 死体遺棄 OR 傷害 OR 銃犯罪 OR 発砲事件 OR 人身取引 OR ストーカー OR 痴漢 OR 売春 OR 援助交際 OR 児童買春 OR わいせつ OR 窃盗 OR 空き巣 OR 車上荒らし OR 万引き OR 脱税 OR 申告漏れ OR データねつ造 OR 背任 OR 爆破 OR ひき逃げ OR 放火 OR 密入国 OR 密輸 OR 密漁 OR 誘拐 OR 拉致 OR 罰金 OR リンチ OR 暴力団 OR 企業舎弟 OR マフィア OR 麻薬 OR アヘン OR ヘロイン OR モルヒネ OR 覚せい剤 OR コカイン OR 大麻 OR ヤクザ OR 容疑 OR 不法 OR 不当要求 OR 反社 OR 特殊知能暴力集団 OR 社会運動標榜ゴロ OR 政治活動標榜ゴロ OR 共生者 OR 事件 OR 違法 OR 違反 OR 疑い OR 偽装 OR 暗躍 OR 行政処分 OR 告訴 OR スキャンダル OR 相場操縦 OR 着服 OR 罪 OR 提訴 OR 判決 OR 不正 OR ブラック OR フロント企業 OR 粉飾 OR 闇 OR 迷惑)) NOT (HL 会社人事 OR 「政府人事」 OR 「自治体人事」 OR HL （死去） OR HL 人事、)) not ＄数表記事'
# 便利関数
def print_html(x):
    print(bs4.BeautifulSoup(x.get_attribute('innerHTML')).prettify())

# ブラウザ起動
browser = webdriver.Chrome()

# 「新聞トレンド」のサイトに移動
URL = 'https://t21.nikkei.co.jp/g3/CMN0F14.do'
# これでログイン入力なしでいける？
# URL = 'https://t21.nikkei.co.jp/g3/CMN0F12.do;jsessionid=34EAE0E4D88ADA430E862F0256522EB7'
browser.get(URL)

# テレコンログイン
login_area = browser.find_element_by_id('membersLogin')
# relogin = browser.find_element_by_class_name('rollover')
# search_area = browser.find_element_by_class_name('nk-home-bundle')

if login_area.is_displayed():
    login_id_input = login_area.find_element_by_name('userId')
    login_pw_input = login_area.find_element_by_name('password')
    login_id_input.send_keys('admin@b-engineer.com')
    login_pw_input.send_keys('bebe1002')
    login_button = login_area.find_element_by_name('submit')
    login_button.click()
    # 念のため5秒待つ
    time.sleep(3)
    if browser.find_element_by_class_name('nk-home-bundle').is_displayed():
        relogin = browser.find_element_by_class_name('nk-home-bundle')
        relogin.click()

# if search_area.is_displayed():
# 「検索ワード入力」欄 -----------------------------
search_area = browser.find_element_by_class_name('nk-home-bundle')

search_input = search_area.find_element_by_class_name('nk-home-bundle-search-input')
search_input.send_keys(sample_word)
time.sleep(3)
# search_input.send_keys(Keys.ENTER)  # x
# time.sleep(3)
# 検索」ボタン
search_btn = search_area.find_element_by_class_name('nk-home-bundle-search-button') # クリックポイントではないと言われる
search_btn.click()
# 念のため5秒待つ
time.sleep(5)

# x見出しを表示ボタン
popup = browser.find_element_by_class_name('nk-popup-ok').send_keys(Keys.ENTER)
print_html(popup)
# highcharts = browser.find_element_by_class_name('highcharts-markers')
#
# # グラフの中身の確認（これが動的に生成されたHTML）
# print_html(highcharts)
#.
#.
# # 動的に生成されたフキダシを取得
# tooltip = browser.find_element_by_class_name('highcharts-tooltip')
#
# # 中身の確認
# print_html(tooltip)
#
# # あとはbeautifulsoupで必要な情報を抽出する
# tooltip_html = bs4.BeautifulSoup(tooltip.get_attribute('innerHTML'))
#.
#.
#.
# # 見づらいのでデータフレーム化
# df = pd.DataFrame(points_info, columns=['期間', 'ごみ', 'キーワード', '記事数']).drop('ごみ', axis=1)
# df
# 後処理
browser.close()
