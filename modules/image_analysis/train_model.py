import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam


import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REAL_PATH = os.path.join(BASE_DIR, "images", "real")
FAKE_PATH = os.path.join(BASE_DIR, "images", "fake")
OUTPUT_REAL = os.path.join(BASE_DIR, "output", "real")
OUTPUT_FAKE = os.path.join(BASE_DIR, "output", "fake")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "images")

# Image generators
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_gen = datagen.flow_from_directory(
    DATA_DIR,
    target_size=(128,128),
    batch_size=16,
    class_mode='binary',
    subset='training'
)

val_gen = datagen.flow_from_directory(
    DATA_DIR,
    target_size=(128,128),
    batch_size=16,
    class_mode='binary',
    subset='validation'
)

# Simple CNN model
model = Sequential([
    Conv2D(32,(3,3),activation='relu', input_shape=(128,128,3)),
    MaxPooling2D(),
    Conv2D(64,(3,3),activation='relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(128,activation='relu'),
    Dense(1,activation='sigmoid')
])

model.compile(optimizer=Adam(0.001), loss='binary_crossentropy', metrics=['accuracy'])

# Train
model.fit(train_gen, validation_data=val_gen, epochs=20)

# Save model
model.save("logo_classifier.h5")
print("✅ Model retrained and saved as logo_classifier.h5")
