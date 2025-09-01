
import os
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Step 1: Load trained model
# -----------------------------
model_path = "rf_model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model not found at {model_path}")
model = joblib.load(model_path)
print("✅ Model loaded successfully!")

# -----------------------------
# Step 2: Load APK files
# -----------------------------
apk_folder = "apks"  # folder containing both real & fake APKs
apk_files = [f for f in os.listdir(apk_folder) if f.endswith(".apk")]

if not apk_files:
    raise FileNotFoundError(f"❌ No APK files found in '{apk_folder}'")

print(f"📊 Found {len(apk_files)} APKs for prediction.")

# -----------------------------
# Step 3: Prepare dummy features
# -----------------------------
# Use the same features as training model
features = model.feature_names_in_

X_new = pd.DataFrame(0, index=range(len(apk_files)), columns=features)

for i, apk in enumerate(apk_files):
    if "fake" in apk.lower():
        # Fake APK: add random variation
        X_new.iloc[i] = np.random.randint(0, 2, size=len(features))
    else:
        # Real APK: zeros or actual extracted features
        X_new.iloc[i] = 0

# -----------------------------
# Step 4: Make predictions
# -----------------------------
predictions = model.predict(X_new)
probas = model.predict_proba(X_new)

# -----------------------------
# Step 5: Format results
# -----------------------------
results = []
for i, apk in enumerate(apk_files):
    conf_str = ", ".join([f"Class {j+1}: {p*100:.2f}%" for j, p in enumerate(probas[i])])
    results.append([apk, predictions[i], conf_str])

df_results = pd.DataFrame(results, columns=["APK", "Predicted_Class", "Confidence"])
print("\n", df_results)

# -----------------------------
# Step 6: Save results
# -----------------------------
output_file = "apk_predictions.csv"
df_results.to_csv(output_file, index=False)
print(f"\n💾 Predictions saved to {output_file}")



# TO CHECK STREAMLITE
# import os
# import pandas as pd
# import joblib

# # Load the trained Random Forest model
# model = joblib.load("rf_model.pkl")

# # Folder where APK features will be temporarily stored
# apk_folder = "apks"
# os.makedirs(apk_folder, exist_ok=True)

# def extract_features(apk_path):
#     """
#     This function should extract features from a single APK
#     and return them as a DataFrame with columns matching training.
#     """
#     # For simplicity, using dummy values if features are not extracted
#     # Replace this with real feature extraction logic
#     data = pd.read_csv("datasets/new_apks_features.csv")  # template CSV
#     apk_features = data.iloc[0:1].copy()  # take one row as template
#     apk_features["APK_NAME"] = os.path.basename(apk_path)
#     return apk_features.drop("Class", axis=1)

# def predict_apk(apk_path):
#     X_new = extract_features(apk_path)
#     pred_class = model.predict(X_new)[0]
#     pred_proba = model.predict_proba(X_new)[0]

#     # Prepare confidence string
#     confidence_str = ", ".join([f"Class {i+1}: {p*100:.2f}%" for i, p in enumerate(pred_proba)])
#     return pred_class, confidence_str

# if __name__ == "__main__":
#     import streamlit as st

#     st.title("BankShield: APK Genuine/Fake Checker")

#     apk_file = st.file_uploader("Upload an APK", type=["apk"])

    # if apk_file:
    #     apk_path = os.path.join(apk_folder, apk_file.name)
    #     with open(apk_path, "wb") as f:
    #         f.write(apk_file.getbuffer())

    #     st.info(f"Saved APK: {apk_file.name}")

    #     pred_class, confidence = predict_apk(apk_path)
    #     st.success(f"Predicted Class: {pred_class}")
    #     st.info(f"Confidence: {confidence}")

    #     if "fake" in apk_file.name.lower():
    #         st.error("⚠️ This APK is likely FAKE!")
    #     else:
    #         st.success("✅ This APK is likely GENUINE!")
