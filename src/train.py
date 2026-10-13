import pandas as pd
import pickle
df = pd.read_csv("data/clean_sales.csv")
total_sales = df["amount"].sum()
model = {
    "total_sales": total_sales,
    "num_rows": len(df)
}
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model saved successfully")
