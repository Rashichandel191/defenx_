from PIL import Image, ImageEnhance, ImageOps
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REAL_DIR = os.path.join(BASE_DIR, "images", "real")
FAKE_DIR = os.path.join(BASE_DIR, "images", "fake")
os.makedirs(FAKE_DIR, exist_ok=True)

# Process each real image
for fname in os.listdir(REAL_DIR):
    img_path = os.path.join(REAL_DIR, fname)
    try:
        img = Image.open(img_path)

        # --- 1. Slight rotation ---
        img_rot = img.rotate(15)
        img_rot.save(os.path.join(FAKE_DIR, "fake_rot_" + fname))

        # --- 2. Color change ---
        img_color = ImageEnhance.Color(img).enhance(0.5)
        img_color.save(os.path.join(FAKE_DIR, "fake_color_" + fname))

        # --- 3. Flip horizontally ---
        img_flip = ImageOps.mirror(img)
        img_flip.save(os.path.join(FAKE_DIR, "fake_flip_" + fname))

        print(f"Processed {fname} -> 3 fake variations created.")

    except Exception as e:
        print(f"Error processing {fname}: {e}")
