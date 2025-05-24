import os
import cv2
import numpy as np
import json

data_dir = "data"  # folder where face images are stored in subfolders named by student ID

faces = []
labels = []

label_map = {}  # label (0,1,2...) to student_id (actual DB id) mapping
current_label = 0

for student_id in os.listdir(data_dir):
    student_path = os.path.join(data_dir, student_id)
    if not os.path.isdir(student_path):
        continue
    label_map[str(current_label)] = int(student_id)  # map current_label to actual student ID

    for image_name in os.listdir(student_path):
        image_path = os.path.join(student_path, image_name)
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue
        faces.append(img)
        labels.append(current_label)
    current_label += 1

faces = np.array(faces)
labels = np.array(labels)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, labels)
recognizer.save("trainer/trainer.yml")

with open("trainer/label_map.json", "w") as f:
    json.dump(label_map, f)

print("Training complete. Label map saved.")
