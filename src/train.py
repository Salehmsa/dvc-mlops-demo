import pandas as pd

df = pd.read_csv("data/sales.csv")

total_sales = df["amount"].sum()

with open("total_sales.txt", "w") as f:
    f.write(f"Total Sales: {total_sales}")

print(f"Total Sales: {total_sales}")