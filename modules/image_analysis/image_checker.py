import cv2
import os

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REAL_PATH = os.path.join(BASE_DIR, "images", "real")
FAKE_PATH = os.path.join(BASE_DIR, "images", "fake")
OUTPUT_REAL = os.path.join(BASE_DIR, "output", "real")
OUTPUT_FAKE = os.path.join(BASE_DIR, "output", "fake")


# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
IMAGES_DIR = os.path.join(BASE_DIR, "images")
REAL_PATH = os.path.join(IMAGES_DIR, "real")
FAKE_PATH = os.path.join(IMAGES_DIR, "fake")

# Output
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(os.path.join(OUTPUT_DIR, "real"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "fake"), exist_ok=True)

def process_and_save(folder_path, label):
    print(f"\n🔍 Looking into folder: {folder_path}")
    if not os.path.exists(folder_path):
        print(f"⚠️ Folder {folder_path} not found!")
        return
    
    files = os.listdir(folder_path)
    print(f"Found {len(files)} files: {files}")
    
    for filename in files:
        img_path = os.path.join(folder_path, filename)
        print(f"➡️ Trying to open {img_path}")
        img = cv2.imread(img_path)

        if img is None:
            print(f"❌ Failed to read {filename}")
            continue

        # Put label text
        color = (0, 255, 0) if label == "REAL" else (0, 0, 255)
        cv2.putText(img, label, (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, color, 2, cv2.LINE_AA)

        # Save output
        out_path = os.path.join(OUTPUT_DIR, label.lower(), filename)
        cv2.imwrite(out_path, img)
        print(f"✅ Saved processed image to {out_path}")

print("🔍 Processing REAL images...")
process_and_save(REAL_PATH, "REAL")

print("\n🔍 Processing FAKE images...")
process_and_save(FAKE_PATH, "FAKE")

print("\n🎉 Done! Check the output folder.")
