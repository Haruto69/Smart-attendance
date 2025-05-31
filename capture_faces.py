import cv2
import os
import sqlite3
from datetime import datetime

DB_PATH = "db.sqlite3"  # Use the Django default DB path

def insert_student(student_id, name):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor.execute(
            "INSERT INTO attendance_student (id, name, registered_on) VALUES (?, ?, ?)",
            (int(student_id), name, now)
        )
        conn.commit()
        print(f"[INFO] Student '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print("[WARNING] Student ID already exists. Skipping insertion.")
    finally:
        conn.close()

def insert_attendance(student_id, teacher_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")
    status = True  # Or False depending on your logic

    try:
        cursor.execute(
            "INSERT INTO attendance_attendance (student_id, date, status, teacher_id) VALUES (?, ?, ?, ?)",
            (int(student_id), today, status, int(teacher_id))
        )
        conn.commit()
        print("[INFO] Attendance recorded successfully.")
    except sqlite3.IntegrityError as e:
        print(f"[WARNING] Could not insert attendance: {e}")
    finally:
        conn.close()

def capture_faces(student_id, name):
    insert_student(student_id, name)

    if not os.path.exists("dataset"):
        os.makedirs("dataset")

    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    count = 0
    while True:
        ret, img = cam.read()
        if not ret:
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            count += 1
            cv2.imwrite(f"dataset/User.{student_id}.{count}.jpg", gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('Capturing Faces', img)

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= 50:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"[INFO] Collected {count} face samples for {name} (ID: {student_id}).")

if __name__ == "__main__":
    sid = input("Enter Student ID (integer): ")
    name = input("Enter Student Name: ")
    if sid.isdigit():
        capture_faces(int(sid), name)
    else:
        print("Invalid ID. Must be an integer.")
