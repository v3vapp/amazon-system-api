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

filename = select_file()

amazon = pd.read_table(filename, encoding = "cp932")
print(amazon.head())

df = pd.DataFrame()

df['お届け先郵便番号']  = amazon["ship-postal-code"]
df['お届け先氏名']     = amazon["recipient-name"]
df['お届け先敬称']     = "様"
df['お届け先住所1行目'] = amazon["ship-state"]
df['お届け先住所2行目'] = amazon["ship-address-1"]
df['お届け先住所3行目'] = amazon["ship-address-2"]
df['お届け先住所4行目'] = amazon["ship-address-3"]
df['内容品']          = "手芸材料"

df = df.drop_duplicates()

tdatetime = dt.now()
now = tdatetime.strftime('%Y-%m-%d')

# os.makedirs("クリックポスト", exist_ok=True)
df.to_csv(f"C:\\Users\\username\\Desktop\\アマゾンシステム\\クリックポスト一括申込\\クリックポスト{now}.csv", encoding = "cp932", index=False)