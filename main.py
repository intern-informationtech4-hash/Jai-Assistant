from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/get-info")
def fetch_data(item: str):
    df = pd.read_csv("sales.csv")
    match = df[df['Product'].str.contains(item, case=False)]
    if match.empty:
        return {"message": "Product nahi mila"}
    return match.to_dict(orient="records")

@app.get("/")
def home():
    return {"status": "Jai is Online"}
