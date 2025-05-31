import cv2
import os
from datetime import datetime
import django
import sys

# Setup Django environment (adjust this path to your Django project root)
sys.path.append(r"C:\\Users\\eng22\\OneDrive\\Desktop\\Smart-attendance-master")  # Use raw string or double backslashes
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendance_system.settings')  # Your Django settings module
django.setup()

from attendance.models import Student, Teacher, Attendance
from django.utils.timezone import now

# Load trained face recognizer model
trainer_path = "trainer/trainer.yml"
if not os.path.exists(trainer_path):
    print("[ERROR] Trainer file not found. Please train the model first.")
    exit()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(trainer_path)

# Load Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Start webcam capture
cap = cv2.VideoCapture(0)

attendance_marked = set()  # Keep track of marked student IDs for this session

while True:
    ret, frame = cap.read()
    if not ret:
        print("[ERROR] Failed to capture frame from camera.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        id_, conf = recognizer.predict(roi_gray)

        # Confidence threshold: tune these values if needed
        if 45 <= conf <= 85:
            try:
                student = Student.objects.get(id=id_)
            except Student.DoesNotExist:
                student = None

            if student and student.id not in attendance_marked:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, student.name, (x, y - 10), font, 1, (0, 255, 0), 2)

                today = now().date()

                # Get any teacher, or handle if none exists
                print("Available teachers:")
                for t in Teacher.objects.all():
                    print("-", t.user.username)

                teacher_username = input("Enter teacher's username: ")
                try:
                    teacher = Teacher.objects.get(user__username=teacher_username)
                    print(f"Attendance will be marked under teacher: {teacher.user.username}")
                except Teacher.DoesNotExist:
                    print("[ERROR] No teacher found with that username.")
                    sys.exit()
                # Mark attendance if not already marked for today
                attendance, created = Attendance.objects.get_or_create(
                    student=student,
                    date=today,
                    teacher=teacher,
                    defaults={'status': True}
                )

                if created:
                    print(f"[INFO] Attendance marked for {student.name} on {today}")
                else:
                    print(f"[INFO] Attendance already marked for {student.name} on {today}")

                attendance_marked.add(student.id)
            else:
                # Student recognized but already marked or no student found
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, "Unknown", (x, y - 10), font, 1, (0, 0, 255), 2)
        else:
            # Face not confidently recognized
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Unknown", (x, y - 10), font, 1, (0, 0, 255), 2)

    cv2.imshow('Face Recognition', frame)

    # Exit if 'q' pressed or at least one attendance marked
    if cv2.waitKey(1) & 0xFF == ord('q') or len(attendance_marked) > 0:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
