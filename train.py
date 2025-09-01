import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from feature_extractor import extract_features_from_dataset

# Step 1: Dataset se features nikalna
dataset_file = "url_list.csv"
features_df = extract_features_from_dataset(dataset_file)
print("Features extracted:", features_df.shape)

# Step 2: Split features (X) and labels (y)
X = features_df.drop("label", axis=1)
y = features_df["label"]

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Report:\n", classification_report(y_test, y_pred))

# Step 6: Save trained model
joblib.dump(model, "fake_url_model.pkl")
print("✅ Model saved as fake_url_model.pkl")
