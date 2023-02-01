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

df_cp = pd.read_csv(filename, encoding = "shift-jis")
print(df_cp.head())


# order-id	
# order-item-id	
# quantity	
# ship-date	
# carrier-code	
# carrier-name	
# tracking-number	
# ship-method	
# cod-collection-method	
# transparency_code	
# ship_from_address_name	
# ship_from_address_line1	
# ship_from_address_line2	
# ship_from_address_line3	
# ship_from_address_city	
# ship_from_address_county	
# ship_from_address_state_or_region	
# ship_from_address_postalcode	
# ship_from_address_countrycode


df = pd.DataFrame()

    df_cp['お届け先郵便番号']  
    df_cp['お届け先氏名']    
    df_cp['お届け先敬称']     
    df_cp['お届け先住所1行目'] 
    df_cp['お届け先住所2行目'] 
    df_cp['お届け先住所3行目']
    df_cp['お届け先住所4行目'] 
    df_cp['内容品']

# I left codes below on the other pc. 
# will be here soon...