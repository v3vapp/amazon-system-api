import pandas as pd
from datetime import datetime as dt
import config

class AmazonCheckSheet:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df_amazon = pd.read_csv(self.file_path, encoding="cp932")

    def generate(self):
        list_purchase_date = []
        list_promise_date = []
        for index, row in self.df_amazon.iterrows():
            list_purchase_date.append(row["purchase-date"])
            list_promise_date.append(row["promise-date"])

        tdatetime = dt.now()
        now = tdatetime.strftime("%m%d")

        df = pd.DataFrame()
        df["購入日"] = list_purchase_date
        df["出荷期限"] = list_promise_date
        df["購入者"] = self.df_amazon["buyer-name"]
        df["宛先"] = self.df_amazon["recipient-name"]
        df["発送方法"] = ""
        df[f"商品名"] = self.df_amazon["product-name"]
        df["個"] = self.df_amazon["quantity-purchased"]
        df["要注文"] = ""
        df["注文済"] = ""
        df["完了"] = ""

        df["購入日"] = pd.to_datetime(df["購入日"])
        df.sort_values(by=["購入日"], inplace=True, ascending=False)
        df["購入日"] = pd.to_datetime(df["購入日"]).dt.strftime("%m-%d %H:%M")
        df["出荷期限"] = pd.to_datetime(df["出荷期限"]).dt.strftime("%m-%d")

        export_path = f"./static/AmazonCheckSheet_{now}.csv"
        df.to_csv(export_path, index=False, encoding="utf-8")

if __name__ == "__main__":
    sheet = AmazonCheckSheet("/home/daiki/Dropbox/v3v/amazon-assistant-api/static/unshipped.txt")
    sheet.generate()
