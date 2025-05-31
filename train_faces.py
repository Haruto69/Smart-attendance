# train_faces.py

import cv2
import numpy as np
from PIL import Image
import os

def train_model():
    # Path to dataset folder
    path = 'dataset'
    
    # Create LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Load the face detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def get_images_and_labels(dataset_path):
        image_paths = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) if f.endswith('.jpg')]
        face_samples = []
        ids = []

        for image_path in image_paths:
            # Open image and convert to grayscale
            pil_img = Image.open(image_path).convert('L')  # Convert to grayscale
            img_numpy = np.array(pil_img, 'uint8')  # Convert PIL image to numpy array

            # Extract ID from filename, assuming filename is like User.<id>.<count>.jpg
            try:
                ida = int(os.path.split(image_path)[-1].split('.')[1])  # Extract student ID from filename
            except ValueError:
                print(f"[WARNING] Skipping file (cannot extract ID): {image_path}")
                continue

            # Detect faces in the image
            faces = detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y+h, x:x+w])
                ids.append(ida)

        return face_samples, ids

    print("[INFO] Training faces...")

    # Get images and labels from dataset
    faces, ids = get_images_and_labels(path)

    # Check if we have any valid faces and IDs
    if len(faces) == 0:
        print("[ERROR] No faces found in the dataset!")
        return

    # Train the recognizer
    recognizer.train(faces, np.array(ids))

    # Create the trainer directory if it doesn't exist
    if not os.path.exists('trainer'):
        os.makedirs('trainer')

    # Save the trained model to a file
    recognizer.save('trainer/trainer.yml')
    print(f"[INFO] Model trained and saved to 'trainer/trainer.yml' with {len(np.unique(ids))} student(s).")

if __name__ == "__main__":
    train_model()
