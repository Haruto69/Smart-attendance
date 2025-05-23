import cv2
import os
import numpy as np
import sqlite3
from datetime import datetime
from PIL import Image

# Load trained model
trainer_path = "trainer/trainer.yml"
if not os.path.exists(trainer_path):
    print("[ERROR] Trainer file not found. Please train the model first.")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(trainer_path)

# Load Haar cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Connect to SQLite DB
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Start video capture
cap = cv2.VideoCapture(0)

attendance_marked = False  # Flag to exit after one successful marking

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        id_, conf = recognizer.predict(roi_gray)

        if conf >= 45 and conf <= 85:
            name = str(id_)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, name, (x, y - 10), font, 1, (0, 255, 0), 2)

            # Mark attendance
            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            cursor.execute("SELECT * FROM attendance WHERE student_id=? AND date=?", (id_, date))
            result = cursor.fetchone()

            if result is None:
                cursor.execute("INSERT INTO attendance (student_id, date, time) VALUES (?, ?, ?)", (id_, date, time))
                conn.commit()
                print(f"[INFO] Attendance marked for ID: {id_} at {time}")
                attendance_marked = True

        else:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Unknown", (x, y - 10), font, 1, (0, 0, 255), 2)

    cv2.imshow('Face Recognition', frame)

    # Exit on 'q' or after attendance is marked
    if cv2.waitKey(1) & 0xFF == ord('q') or attendance_marked:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
conn.close()
