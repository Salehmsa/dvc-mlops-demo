import pandas as pd
df = pd.read_csv("data/sales.csv")
df = df.drop_duplicates()
df.to_csv("data/clean_sales.csv", index=False)
print("Data cleaned successfully")