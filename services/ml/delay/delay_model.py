import joblib
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

MODULE_DIR = Path(__file__).resolve().parent
DATA_PATH = MODULE_DIR / "delay_data.csv"
MODEL_PATH = MODULE_DIR / "delay.pkl"


def train_delay_model():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing delay training data: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    X = df[["distance", "traffic", "weather"]]
    y = df["delayed"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    return "Delay model trained"


def predict_delay(distance, traffic, weather):
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Delay model not found: {MODEL_PATH}. Run training first.")

    model = joblib.load(MODEL_PATH)

    pred = model.predict([[distance, traffic, weather]])
    return {"delayed": bool(pred[0])}
