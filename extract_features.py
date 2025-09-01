import os
import pandas as pd

# -----------------------------
# Step 0: Define your feature columns (470 features)
# Use the same list you used for training
columns = [
    'ACCESS_PERSONAL_INFO___', 'ALTER_PHONE_STATE___', 'ANTI_DEBUG_____', 'CREATE_FOLDER_____', 
    'CREATE_PROCESS`_____', 'CREATE_THREAD_____', 'DEVICE_ACCESS_____', 'EXECUTE_____', 
    # ... (all remaining 470 feature names) ...
    'write'
]

# -----------------------------
# Step 1: APK folders
apk_folders = ["apks", "fake_apks"]  # genuine + fake APKs
all_apk_files = []

for folder in apk_folders:
    for file in os.listdir(folder):
        if file.endswith(".apk"):
            all_apk_files.append(os.path.join(folder, file))

print(f"✅ Found {len(all_apk_files)} APKs for feature extraction")

# -----------------------------
# Step 2: Create empty DataFrame with columns
df = pd.DataFrame(columns=columns + ["APK"])  # add APK name as last column

# -----------------------------
# Step 3: Feature extraction (dummy/example values)
# Replace this with your real feature extraction logic
for apk_path in all_apk_files:
    apk_name = os.path.basename(apk_path)
    
    # Dummy features: replace with your actual extraction logic
    features = [0] * len(columns)
    
    # Append to DataFrame
    df.loc[len(df)] = features + [apk_name]

# -----------------------------
# Step 4: Save to CSV
os.makedirs("datasets", exist_ok=True)
df.to_csv("datasets/new_apks_features.csv", index=False)
print("💾 Features CSV created with both genuine and fake APKs!")
