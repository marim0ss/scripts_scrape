# https://tonari-it.com/python-scraping-phantomjs-cloud/
import json
import urllib.parse # URL関係を操作
import requests
import bs4

payload = {'url':'https://www.j-platpat.inpit.go.jp/s0100','renderType':'HTML','outputAsJson':'true'}
payload = json.dumps(payload) #JSONパース
payload = urllib.parse.quote(payload,safe = '') #URIエンコード PhantomJS Cloudでは「/」もエンコードする必要がある
# print(payload)

# phantomjsのアクセスキー
key = 'ak-d7x32-qvry0-7xxcc-qsyrq-qf39t'
url = "https://phantomjscloud.com/api/browser/v2/"+ key+"/?request=" + payload

response = requests.get(url) #GETリクエスト
# requests.get関数の戻り値のResponseオブジェクトからデータを取り出すときはこのようにする
# print(response.text)
# PhantomJs Cloudから返ってきたデータはJSON形式なので、Pythonで扱いやすいように辞書型に変換する必要があります。
responseDict = response.json()
html = responseDict["content"]["data"]
# print(html)
soup = bs4.BeautifulSoup(html, "html.parser")
print(soup.form)
