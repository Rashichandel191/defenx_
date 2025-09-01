import joblib
import numpy as np
import pandas as pd
import os
from image_analysis import image_checker
from url_analysis import url_checker
from apk_analysis import apk_checker



MODEL_PATH = os.path.join("models", "rf_model.pkl")
model = joblib.load(MODEL_PATH)

def extract_dummy_features(apk_name: str):
    """For now: create dummy features. Replace later with actual extractor."""
    features = model.feature_names_in_
    row = np.zeros(len(features))
    if "fake" in apk_name.lower():
        row = np.random.randint(0, 2, size=len(features))
    return pd.DataFrame([row], columns=features)

def check_apk(file):
    X = extract_dummy_features(file.filename)
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0].max()
    return {
        "filename": file.filename,
        "prediction": "Fake APK" if pred == 1 else "Genuine APK",
        "confidence": round(proba*100, 2)
    }
