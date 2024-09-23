import pandas as pd

bm = pd.read_csv("big-mac-full-index.csv")

# for index, row in bm.iterrows():
#     print(row["date"], row["iso_a3"], row["currency_code"])

print(bm.apply(lambda row: row["date"], axis = 1))