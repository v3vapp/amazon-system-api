import pandas as pd
from datetime import datetime as dt
import os
from module import select_file

filename = select_file()

amazon = pd.read_table(filename, encoding = "shift-jis")
print(amazon.head())

df = pd.DataFrame()

df['お届け先郵便番号']  = amazon["ship-postal-code"]
df['お届け先氏名']     = amazon["recipient-name"]
df['お届け先敬称']     = "様"
df['お届け先住所1行目'] = amazon["ship-state"]
df['お届け先住所2行目'] = amazon["ship-address-1"]
df['お届け先住所3行目'] = amazon["ship-address-2"]
df['お届け先住所4行目'] = amazon["ship-address-3"]
df['内容品']          = "雑貨など"

tdatetime = dt.now()
now = tdatetime.strftime('%Y年%m月%d日')

os.makedirs("dist/clickpost/", exist_ok=True)
df.to_csv(f"dist/clickpost/clickpost{now}.csv", encoding = "shift-jis", index=False)