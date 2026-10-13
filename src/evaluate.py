import pickle
import json
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)
metrics = {
    "total_sales": int(model["total_sales"]),
    "num_rows": int(model["num_rows"])
}
with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)
print("Metrics saved")