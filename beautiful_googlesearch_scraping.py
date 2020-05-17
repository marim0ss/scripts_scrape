#coding: UTF-8
from urllib import request
from bs4 import BeautifulSoup
import requests
# import urllib.parse
import pprint  # pprint.pprint()で出力が改行されて見やすくなる

def scraping():
    #url
    url = "https://www.google.com/search?lr=&as_qdr=all&ei=Rhq-XpKTIom2mAWE8ok4&q=%E5%90%89%E7%80%AC%E7%A4%BC+%E8%A1%8C%E6%94%BF%E6%8C%87%E5%B0%8E+OR+%E9%80%81%E6%A4%9C+OR+%E6%8D%9C%E6%9F%BB+OR+%E9%80%AE%E6%8D%95+OR+%E3%82%A4%E3%83%B3%E3%82%B5%E3%82%A4%E3%83%80%E3%83%BC+OR+%E6%9E%B6%E7%A9%BA+OR+%E8%84%B1%E7%A8%8E+OR+%E7%94%B3%E5%91%8A%E6%BC%8F%E3%82%8C+OR+%E7%BD%B0%E9%87%91+OR+%E6%9A%B4%E5%8A%9B%E5%9B%A3+OR+%E3%83%A4%E3%82%AF%E3%82%B6+OR+%E5%AE%B9%E7%96%91+OR+%E5%8F%8D%E7%A4%BE+OR+OR+OR+%E4%BA%8B%E4%BB%B6+OR+%E9%81%95%E6%B3%95+OR+%E9%81%95%E5%8F%8D+OR+%E7%96%91%E3%81%84+OR+%E5%81%BD%E8%A3%85+OR+%E8%A1%8C%E6%94%BF%E5%87%A6%E5%88%86+OR+%E5%91%8A%E8%A8%B4+OR+%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%80%E3%83%AB+OR+%E7%BD%AA+OR+%E4%B8%8D%E6%AD%A3+OR+%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF+OR+%E7%B2%89%E9%A3%BE+OR+%E8%BF%B7%E6%83%91&oq=%E5%90%89%E7%80%AC%E7%A4%BC+%E8%A1%8C%E6%94%BF%E6%8C%87%E5%B0%8E+OR+%E9%80%81%E6%A4%9C+OR+%E6%8D%9C%E6%9F%BB+OR+%E9%80%AE%E6%8D%95+OR+%E3%82%A4%E3%83%B3%E3%82%B5%E3%82%A4%E3%83%80%E3%83%BC+OR+%E6%9E%B6%E7%A9%BA+OR+%E8%84%B1%E7%A8%8E+OR+%E7%94%B3%E5%91%8A%E6%BC%8F%E3%82%8C+OR+%E7%BD%B0%E9%87%91+OR+%E6%9A%B4%E5%8A%9B%E5%9B%A3+OR+%E3%83%A4%E3%82%AF%E3%82%B6+OR+%E5%AE%B9%E7%96%91+OR+%E5%8F%8D%E7%A4%BE+OR+OR+OR+%E4%BA%8B%E4%BB%B6+OR+%E9%81%95%E6%B3%95+OR+%E9%81%95%E5%8F%8D+OR+%E7%96%91%E3%81%84+OR+%E5%81%BD%E8%A3%85+OR+%E8%A1%8C%E6%94%BF%E5%87%A6%E5%88%86+OR+%E5%91%8A%E8%A8%B4+OR+%E3%82%B9%E3%82%AD%E3%83%A3%E3%83%B3%E3%83%80%E3%83%AB+OR+%E7%BD%AA+OR+%E4%B8%8D%E6%AD%A3+OR+%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF+OR+%E7%B2%89%E9%A3%BE+OR+%E8%BF%B7%E6%83%91&gs_lcp=CgZwc3ktYWIQA1C0lhVYg58VYOihFWgAcAB4AIABAIgBAJIBAJgBAqABAaABAqoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwiSzrzjg7XpAhUJG6YKHQR5AgcQ4dUDCAw&uact=5"

    #get html
    html = requests.get(url).text
    # html = urllib.request.urlopen(url)

    #set BueatifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)

    # #get headlines
    result_stats = soup.find("div", attrs={"id", "result-stats"})
    print(result_stats)
    # headlines = mainNewsIndex.find_all("div", attrs={"class", "p-list-item__inner"})
    #
    # #print headlines
    # for title in headlines:
    #     print(type(title))              # type()は型の確認
    #     # ログ見方：捕獲データ、対応した箇所のHTML部分の順に出力
    #     pprint.pprint(title.__dict__)   # リスト（list型）や辞書（dict型）
    #     print(title.contents[1].string) # titleの中から指定のタグの中身を表示
    #     print(title.time.string)        # 時刻


if __name__ == "__main__":
    scraping()
