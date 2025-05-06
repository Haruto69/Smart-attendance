import cv2
import os
import numpy as np
from PIL import Image
import pickle

# Path to the trainer file (model)
trainer_path = "trainer/trainer.yml"

# Create face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Check if the trainer file exists
if not os.path.exists(trainer_path):
    print("[ERROR] Trainer file not found. Please train the model first.")
    exit()

# Load the trained model
recognizer.read(trainer_path)

# Load the cascade for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Get the face region
        roi_gray = gray[y:y + h, x:x + w]

        # Predict the label of the face
        id_, conf = recognizer.predict(roi_gray)

        # If confidence is less than 100, consider it a match
        if conf >= 45 and conf <= 85:
            # Display the predicted name (ID)
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = str(id_)
            cv2.putText(frame, name, (x, y - 10), font, 1, (0, 255, 0), 2)
        else:
            # Display "Unknown" if the confidence is too low
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = "Unknown"
            cv2.putText(frame, name, (x, y - 10), font, 1, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow('Face Recognition', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
