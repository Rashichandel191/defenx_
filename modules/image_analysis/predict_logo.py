import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "logo_classifier.h5")
REAL_DIR = os.path.join(BASE_DIR, "images", "real")
FAKE_DIR = os.path.join(BASE_DIR, "images", "fake")
TEST_DIR = os.path.join(BASE_DIR, "test_images")  # New folder for manual testing

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REAL_PATH = os.path.join(BASE_DIR, "images", "real")
FAKE_PATH = os.path.join(BASE_DIR, "images", "fake")
OUTPUT_REAL = os.path.join(BASE_DIR, "output", "real")
OUTPUT_FAKE = os.path.join(BASE_DIR, "output", "fake")


# --- Load Model ---
print("🔍 Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
IMG_SIZE = (128, 128)

def predict_logo(img_path):
    img = image.load_img(img_path, target_size=IMG_SIZE)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array, verbose=0)[0][0]
    if prediction > 0.5:
        return f"✅ REAL Logo ({prediction:.2f})"
    else:
        return f"❌ FAKE Logo ({prediction:.2f})"

# --- Test sample dataset ---
print("\n📂 Testing REAL images:")
for fname in os.listdir(REAL_DIR)[:3]:
    fpath = os.path.join(REAL_DIR, fname)
    print(fname, "->", predict_logo(fpath))

print("\n📂 Testing FAKE images:")
for fname in os.listdir(FAKE_DIR)[:3]:
    fpath = os.path.join(FAKE_DIR, fname)
    print(fname, "->", predict_logo(fpath))

# --- Auto-test all images in test_images/ ---
if not os.path.exists(TEST_DIR):
    os.makedirs(TEST_DIR)

test_files = os.listdir(TEST_DIR)
if test_files:
    print("\n🖼️ Predicting all images in test_images/ folder:")
    for fname in test_files:
        fpath = os.path.join(TEST_DIR, fname)
        print(fname, "->", predict_logo(fpath))
else:
    print("\n📂 test_images/ folder is empty. Drop logos here for auto-prediction.")
