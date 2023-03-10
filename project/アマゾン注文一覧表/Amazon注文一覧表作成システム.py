import pandas as pd
from datetime import datetime as dt
import os
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

from tkinter import filedialog, Tk
import platform
import numpy as np

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

filename = select_file()

df_amazon = pd.read_table(filename, encoding = "cp932")

list_purchase_date = []
list_promise_date = []

for index, row in df_amazon.iterrows():
    list_purchase_date.append(row["purchase-date"])
    list_promise_date.append(row["promise-date"])

# list_purchase_date_simple = []
# list_promise_date_simple = []
# for purchase_date, promise_date in zip(list_purchase_date,list_promise_date):
#     list_purchase_date_simple.append(purchase_date[5:10])
#     list_promise_date_simple.append(promise_date[5:10])
    

tdatetime = dt.now()
now = tdatetime.strftime('%Y-%m-%d')

df = pd.DataFrame()
# df['購入日']   = list_purchase_date_simple
# df['出荷期限'] = list_promise_date_simple
df['購入日']   = list_purchase_date
df['出荷期限'] = list_promise_date

df['購入者']   = df_amazon["buyer-name"]
df['宛先']     = df_amazon["recipient-name"]

df[f'商品名'] = df_amazon["product-name"]
df['個']      = df_amazon["quantity-purchased"]

df['要注文'] = ""
df['注文済'] = ""
df['完了']   = ""

df['発送方法'] = "普・外・CP・LP・特・ゆうP・他"

df['購入日'] = pd.to_datetime(df['購入日'])
df.sort_values(by=['購入日'], inplace=True, ascending=False)


# df = df.iloc[::-1]

# df.reset_index(drop=True, inplace=True)

# df.index = np.arange(1, len(df)+1)
# print(df)

df.to_csv(f"C:\\Users\\user\\Desktop\\アマゾンシステム\\アマゾン注文一覧表\\注文一覧表{now}.csv", index = False, encoding = "cp932")