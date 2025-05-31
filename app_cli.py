# app_cli.py

import capture_faces
import train_faces
import recognize_and_mark
import view_attendance

def register_student():
    capture_faces.register_student()

def train_model():
    train_faces.train_model()

def take_attendance():
    recognize_and_mark.recognize_and_mark_attendance()

def view_records():
    view_attendance.view_attendance()

def main():
    while True:
        print("Face Recognition Attendance System")
        print("1. Register New Student")
        print("2. Train Face Recognizer")
        print("3. Take Attendance")
        print("4. View Attendance")
        print("5. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            register_student()
        elif choice == '2':
            train_model()
        elif choice == '3':
            take_attendance()
        elif choice == '4':
            view_records()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
