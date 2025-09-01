# model.py
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
import os

MODEL_PATH = "fake_app_model.pkl"

def load_or_train_model():
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
    else:
        np.random.seed(42)
        data = pd.DataFrame({
            "downloads": np.random.randint(100, 1000000, 500),
            "rating": np.random.uniform(1, 5, 500),
            "size": np.random.randint(5, 200, 500),
            "sms_permission": np.random.randint(0, 2, 500),
            "accessibility_permission": np.random.randint(0, 2, 500),
            "overlay_permission": np.random.randint(0, 2, 500),
            "label": np.random.randint(0, 2, 500)
        })
        X, y = data.drop("label", axis=1), data["label"]
        model = RandomForestClassifier()
        model.fit(X, y)
        joblib.dump(model, MODEL_PATH)
    return model
