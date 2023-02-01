import pandas as pd
from datetime import datetime as dt
import config

def generate(file_path):

    df_amazon = pd.read_csv(file_path, encoding = "cp932")

    # print(df_amazon)

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
    now = tdatetime.strftime('%m%d')

    df = pd.DataFrame()
    # df['購入日']   = list_purchase_date_simple
    # df['出荷期限'] = list_promise_date_simple
    df['購入日'] = list_purchase_date

    df['出荷期限'] = list_promise_date

    df['購入者'] = df_amazon["buyer-name"]
    df['宛先'] = df_amazon["recipient-name"]
    df['発送方法'] = ""

    df[f'商品名'] = df_amazon["product-name"]
    df['個'] = df_amazon["quantity-purchased"]

    df['要注文'] = ""
    df['注文済'] = ""
    df['完了'] = ""


    df['購入日'] = pd.to_datetime(df['購入日'])
    df.sort_values(by=['購入日'], inplace=True, ascending=False)

    df['購入日'] = pd.to_datetime(df['購入日']).dt.strftime('%m-%d %H:%M')
    # df['購入日'] = df['購入日'].dt.strftime('%m-%d %H:%M')

    df['出荷期限'] = pd.to_datetime(df['出荷期限']).dt.strftime('%m-%d')
    # df['出荷期限'] = df['出荷期限'].dt.strftime('%m-%d')


    # df = df.iloc[::-1]

    # df.reset_index(drop=True, inplace=True)

    # df.index = np.arange(1, len(df)+1)
    # print(df)

    export_path = f"./static/AmazonCheckSheet_{now}.csv"
    df.to_csv(export_path, index = False, encoding = "cp932")

#----------------------------------------------------------------------------------------

if __name__ == "__main__":

    generate("/home/daiki/Dropbox/v3v/amazon-assistant-api/sample/12345.txt")