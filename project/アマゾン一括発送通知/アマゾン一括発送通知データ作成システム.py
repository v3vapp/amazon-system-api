import pandas as pd
from datetime import datetime as dt
import os
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

from tkinter import filedialog, Tk
import platform

from pathlib import Path
# ダイアログ用のルートウィンドウの作成
root = Tk()
# ウィンドウサイズを0にする（Windows用の設定）
root.geometry("0x0")
# ウィンドウのタイトルバーを消す（Windows用の設定）
root.overrideredirect(1)
# ウィンドウを非表示に
root.withdraw()
system = platform.system()

def select_file():
    # Windowsの場合withdrawの状態だとダイアログも
    # 非表示になるため、rootウィンドウを表示する
    if system == "Windows":
        root.deiconify()
    # macOS用にダイアログ作成前後でupdate()を呼ぶ
    root.update()
    # ダイアログを前面に
    root.lift()
    root.focus_force()
    path_str = filedialog.askopenfilename()
    root.update()
    if system == "Windows":
        # 再度非表示化（Windowsのみ）
        root.withdraw()
    path = Path(path_str)
    return path.absolute()

print("\nAmazonからダウンロードした【注文レポート（数字が羅列されたファイル）】ファイルを選択してください。")
# create track data df
amazon_file = select_file()
df_amazon = pd.read_table(amazon_file, encoding = "cp932")

df_trackId = pd.read_csv(r"C:\Users\username\Desktop\アマゾンシステム\アマゾン一括発送通知\一括通知希望リスト.csv",encoding = "cp932")

#_________________________________________________________________________________________

list_buyer = df_amazon["buyer-name"]
 
visited = set()
dup = {x for x in list_buyer if x in visited or (visited.add(x) or False)}

print("\n【複数注文した購入者】を表示します。通知が漏れに注意してください。\n")
for i in dup:
    print(i) 
print()
print()

df_amazon = df_amazon.drop_duplicates(subset=['buyer-email'])

# print(df_trackId.head())

list_TrackID    = list(df_trackId['追跡番号'])
list_Name       = list(df_trackId['宛名'])

list_order_id = []

for index, row in df_amazon.iterrows():
    for name in list_Name:
        if row["recipient-name"] == name:
            list_order_id.append(row["order-id"])

# for i,t, o in zip(list_Name, list_TrackID, list_order_id):
#     print(f"{i}->{t} is {o}")

tdatetime = dt.now()
now = tdatetime.strftime('%Y-%m-%d')

tdatetime = dt.now()
now_for_df = tdatetime.strftime('%Y-%m-%dT%H:%M:%S+09:00')

# df_trackId['注文番号'] = list_order_id

# df_trackId['出荷日'] = now_for_df
# df_trackId['お問い合わせ番号']= df_trackId['追跡番号']

# df_trackId = df_trackId.drop(columns=['宛名',"追跡番号"])

# df_trackId.reindex(columns=["注文番号", "注文商品番号", "出荷数", "出荷日", '配送業者コード','配送業者名','お問い合わせ番号','配送方法' ])

df_ship = pd.DataFrame()
df_ship["注文番号"] = list_order_id
df_ship["注文商品番号"] = ""
df_ship["出荷数"] =  ""
df_ship["出荷日"] = now_for_df
df_ship['配送業者コード'] = "Japan Post"
df_ship['配送業者名'] = ""
df_ship['お問い合わせ伝票番号'] = df_trackId['追跡番号']
df_ship['配送方法'] = "クリックポスト"

df_ship.to_csv(f"C:\\Users\\user\\Desktop\\アマゾンシステム\\アマゾン一括発送通知\\アマゾン一括通知コピー用{now}.csv", encoding = "cp932", index=False)

print("発送通知用のデータを作成完了。【一括通知アップロード】ファイルにコピーしてご利用ください。\n")