#coding: UTF-8
from urllib import request
from bs4 import BeautifulSoup
import urllib.parse
import pprint  # pprint.pprint()で出力が改行されて見やすくなる

def scraping():
    #url
    url = "https://www.google.com/search"
    seach_word = 'クロスフォー'

    encodeWord = urllib.parse.quote(seach_word)
    url = url + '?as_q=' + encodeWord #+ '&as_oq=' + CHECK_WORD

    #get html
    html = request.urlopen(url)

    #set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    # #get headlines
    # mainNewsIndex = soup.find("ul", attrs={"class", "p-category-latest-sec-list"})
    # headlines = mainNewsIndex.find_all("div", attrs={"class", "p-list-item__inner"})
    #
    # #print headlines
    # for title in headlines:
    #     print(type(title))              # type()は型の確認
    #     # ログ見方：捕獲データ、対応した箇所のHTML部分の順に出力
    #     pprint.pprint(title.__dict__)   # リスト（list型）や辞書（dict型）
    #     print(title.contents[1].string) # titleの中から指定のタグの中身を表示
    #     print(title.time.string)        # 時刻


# if __name__ == "__main__":
    # scraping()
