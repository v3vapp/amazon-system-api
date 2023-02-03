import pandas as pd
from datetime import datetime as dt
# from app.config import root

class AmazonCheckSheet:
    def __init__(self, file_path_unshipped, file_path_neworder):

        self.file_path_unshipped = file_path_unshipped
        self.file_path_neworder = file_path_neworder

        self.df_main = pd.read_table(self.file_path_unshipped, encoding="cp932")
        self.df_price = pd.read_table(self.file_path_neworder, encoding="cp932")

        print(self.df_price)

    def generate(self):
    
        df = pd.DataFrame()
        df["注文ID"]   = self.df_main["order-id"]

        df["購入日"]   = self.df_main["purchase-date"]
        df["出荷期限"]  = self.df_main["promise-date"]

        # Purchase date
        df["購入日"] = pd.to_datetime(df["購入日"])
        df.sort_values(by=["購入日"], inplace=True, ascending=False)
        df["購入日"] = df["購入日"].dt.tz_convert('Asia/Tokyo')
        df["購入日"] = df["購入日"].dt.strftime("%m-%d %H:%M")
        # Ship Limit Date
        df["出荷期限"] = pd.to_datetime(df["出荷期限"])
        df["出荷期限"] = df["出荷期限"].dt.tz_convert('Asia/Tokyo')
        df["出荷期限"] = df["出荷期限"].dt.strftime("%m-%d")
        
        # df["購入日 & 〆切"]   = df[['購入日', '出荷期限']].agg(' 〆'.join, axis=1)

        df["購入者"]   = self.df_main["buyer-name"]
        df["宛名"]     = self.df_main["recipient-name"]

        # df["購入者-> 宛名"]   = df[['購入者', '宛名']].agg(' > '.join, axis=1)

        df["発送方法"]  = ""

        self.df_price["total-cost"] = self.df_price["item-price"]+\
                                            self.df_price["shipping-price"]+\
                                                self.df_price["item-tax"]+\
                                                    self.df_price["shipping-tax"]
        for i, row in df.iterrows():
            main_oid = row["注文ID"]

            for _, rowrow in self.df_price.iterrows():
                price_oid = rowrow["order-id"]

                paid = rowrow["total-cost"]

                if main_oid == price_oid:
                    df.loc[i, "支払金額"] = paid

        # df["商品名 @SKU"]   = self.df_main[['product-name', 'sku']].agg(' @'.join, axis=1)
        
        df["商品名"]   = self.df_main['product-name']
        df["個"]      = self.df_main["quantity-purchased"]

        df["SKU"]     = self.df_main["sku"]
        df["要注文"]   = ""
        df["注文済"]   = ""
        df["完了"]     = ""

        # df.drop(columns=['購入日', "出荷期限", "SKU", "宛名", "購入者" ], inplace=True)

        now = dt.now().strftime("%m%d")

        export_filename = f"AmazonCheckSheet_{now}.csv"

        export_path = f"./static/{export_filename}"
        df.to_csv(export_path, index=False, encoding="utf-8")

        return export_filename

if __name__ == "__main__":
    sheet = AmazonCheckSheet("/home/daiki/Downloads/10079880679019391.txt", "/home/daiki/Downloads/10077229079019391.txt")
    sheet.generate()
