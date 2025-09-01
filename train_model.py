import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# -----------------------------
# Step 1: Load dataset safely
# -----------------------------
folders = ["dataset", "datasets"]
file_name = "feature_vectors_syscallsbinders_frequency_5_Cat.csv"

data = None
for folder in folders:
    file_path = os.path.join(folder, file_name)
    if os.path.exists(file_path):
        print(f"✅ File found at: {file_path}")
        data = pd.read_csv(file_path)
        break

if data is None:
    raise FileNotFoundError(f"❌ File not found! Check that '{file_name}' is in one of these folders: {folders}")

# -----------------------------
# Step 2: Define features & target
# -----------------------------
# Tumhara target column 'Class' hai
X = data.drop("Class", axis=1)  # features
y = data["Class"]               # target

print(f"\n📊 Features shape: {X.shape}")
print(f"📊 Target shape: {y.shape}")

# -----------------------------
# Step 3: Split dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# Step 4: Train Random Forest
# -----------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------------
# Step 5: Evaluate model
# -----------------------------
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n✅ Accuracy: {acc*100:.2f}%")
print("\n📄 Classification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# Step 6: Save model (optional)
# -----------------------------
import joblib
joblib.dump(model, "rf_model.pkl")
print("\n💾 Model saved as 'rf_model.pkl'")
