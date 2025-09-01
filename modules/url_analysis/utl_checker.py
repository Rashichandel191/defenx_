import joblib
import pandas as pd
import re
import os

MODEL_PATH = os.path.join("models", "fake_url_model.pkl")
model = joblib.load(MODEL_PATH)

def simple_features(url: str):
    return {
        "url_length": len(url),
        "num_digits": sum(c.isdigit() for c in url),
        "num_special": len(re.findall(r"[^A-Za-z0-9:/._-]", url)),
        "has_https": 1 if url.startswith("https://") else 0,
        "has_at": 1 if "@" in url else 0,
        "has_ip": 1 if re.search(r"(?:\d{1,3}\.){3}\d{1,3}", url) else 0,
        "num_subdomains": url.count("."),
    }

def check_url(url: str):
    feats = simple_features(url)
    X = pd.DataFrame([feats])
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0].max()
    return {
        "url": url,
        "prediction": "Fake URL" if pred==1 else "Genuine URL",
        "confidence": round(proba*100,2)
    }
