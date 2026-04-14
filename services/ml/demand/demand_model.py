import joblib
from pathlib import Path

import pandas as pd
from prophet import Prophet

MODULE_DIR = Path(__file__).resolve().parent
DATA_PATH = MODULE_DIR / "sales_data.csv"
MODEL_PATH = MODULE_DIR / "demand.pkl"


def train_demand_model():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing demand training data: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    df = df.rename(columns={"date": "ds", "sales": "y"})

    model = Prophet()
    model.fit(df)

    joblib.dump(model, MODEL_PATH)
    return "Demand model trained"


def predict_demand(days=7):
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Demand model not found: {MODEL_PATH}. Run training first.")

    model = joblib.load(MODEL_PATH)

    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)

    return forecast[["ds", "yhat"]].tail(days).to_dict(orient="records")
