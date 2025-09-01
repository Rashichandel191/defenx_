import pandas as pd
import joblib

# 1️⃣ Load trained model
model = joblib.load("rf_model.pkl")
print("✅ Model loaded successfully!")

# 2️⃣ Load your new APK features CSV
new_apks_df = pd.read_csv("datasets/new_apks_features.csv")
print(f"📊 Loaded {len(new_apks_df)} APKs for prediction.")

# 3️⃣ Full list of 470 features used in training
all_features = [
    'ACCESS_PERSONAL_INFO___', 'ALTER_PHONE_STATE___', 'ANTI_DEBUG_____', 'CREATE_FOLDER_____', 
    'CREATE_PROCESS`_____', 'CREATE_THREAD_____', 'DEVICE_ACCESS_____', 'EXECUTE_____', 
    # ... (all 470 features exactly as in training)
    'write'
]

# 4️⃣ Ensure CSV has all required columns
for col in all_features:
    if col not in new_apks_df.columns:
        new_apks_df[col] = 0  # missing columns filled with 0

# 5️⃣ Keep only columns needed and in correct order
X_new = new_apks_df[all_features]

# 6️⃣ Make predictions
predictions = model.predict(X_new)
probabilities = model.predict_proba(X_new)

# 7️⃣ Display predictions
for i, apk_name in enumerate(new_apks_df.get('APK_NAME', range(len(X_new)))):
    print(f"APK: {apk_name} -> Prediction: {predictions[i]}, Confidence: {max(probabilities[i])*100:.2f}%")
