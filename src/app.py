from fastapi import FastAPI
import pickle

app = FastAPI()

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "DVC MLOps API"}

@app.get("/predict/{amount}")
def predict(amount: int):
    average = model["total_sales"] / model["num_rows"]

    return {
        "input": amount,
        "prediction": float(average + amount)
    }