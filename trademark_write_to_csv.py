import pandas as pd
import pprint

# 元の文字列
s = """
Ｃａｒｅｅｒ Ｂｏｏｓｔ
Ｔｅｃｈ Ｓｔａｒｓ
イッカツ
ＭＩＤＷＯＲＫＳ
ＣａｒｅｅｒＴＶ
ウラナル
ｍａｙｏｎｅｚ
ｔｅｃｈ ｂｏｏｓｔ
ＢＲＡＮＤＩＮＧ ＥＮＧＩＮＥＥＲ
§Ｂ＼Ｅ∞ＢＲＡＮＤＩＮＧ＼ＥＮＧＩＮＥＥＲ
ＤＩＧＧ
ＭｕｇｅｎＷｏｒｋｓ
"""
list = s.split() # 文字列をリスト化
# print(list)

# データフレーム作る
columns = ["name"]
df = pd.DataFrame(columns=columns) # 列名を指定する
# print(df) # 空ののdf作成

for name in list:
    # print(name)
    # 行の作成
    se = pd.Series([name], columns)
    print(se)
    df = df.append(se, columns) # データフレームに行を追加
print(df)

filename = 'trademark_names.csv'
df.to_csv(filename, encoding = 'utf-8')
print('⭐️⭐️⭐️ csvファイルを出力しました ⭐️⭐️⭐️')