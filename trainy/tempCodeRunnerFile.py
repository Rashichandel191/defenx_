# app_flask.py
from flask import Flask, render_template, request, jsonify

import pandas as pd
import joblib
from model import load_or_train_model

app = Flask(__name__)
model = load_or_train_model()

@app.route('/')
def home():
    return render_template('index.html')  # We'll create a simple HTML page with iframe

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = pd.DataFrame([{
        "downloads": data.get("downloads", 0),
        "rating": data.get("rating", 0.0),
        "size": data.get("size", 1),
        "sms_permission": 1 if "SMS" in data.get("permissions", []) else 0,
        "accessibility_permission": 1 if "Accessibility" in data.get("permissions", []) else 0,
        "overlay_permission": 1 if "Overlay" in data.get("permissions", []) else 0
    }])
    
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0][1]
    
    result = {
        "prediction": int(prediction),
        "confidence": float(proba)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
