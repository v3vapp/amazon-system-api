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

filename = "/home/daiki/Downloads/unship.txt"

df_amazon = pd.read_table(filename, encoding = "cp932")

tdatetime = dt.now()
now = tdatetime.strftime('%Y-%m-%d')

df = pd.DataFrame()

df['宛先1']    = ""
df['宛先2']    = df_amazon["recipient-name"]
df['郵便番号']  = df_amazon["ship-postal-code"]

df['住所1']    = df_amazon["ship-address-1"]
df['住所2']    = df_amazon["ship-address-2"].str.cat(df_amazon["ship-address-3"], sep=" ")
df['電話番号']  = ""
df['品名']     = "手芸材料"

df.to_csv(f"C:\\Users\\username\\Desktop\\アマゾンシステム\\レターパック\\作成データ\\レターパック_{now}.csv", encoding = "cp932", index=False)
