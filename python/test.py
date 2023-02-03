import pandas as pd

df = pd.read_table("/home/daiki/Downloads/10078942795019391.txt", encoding="cp932")

print(df["item-price"])

print(df["item-price"]+df["shipping-price"]+df["item-tax"]+df["shipping-tax"])