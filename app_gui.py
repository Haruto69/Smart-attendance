# app_gui.py

import tkinter as tk
from tkinter import messagebox
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

def exit_app():
    if messagebox.askokcancel("Exit", "Do you really want to quit?"):
        window.destroy()

window = tk.Tk()
window.title("Face Recognition Attendance System")
window.geometry("500x400")
window.config(bg="#1c1c1c")

tk.Label(
    window,
    text="Face Attendance System",
    font=("Verdana", 20, "bold"),
    fg="yellow",
    bg="#1c1c1c"
).pack(pady=20)

tk.Button(
    window,
    text="Register New Student",
    command=register_student,
    font=("Verdana", 14),
    bg="black",
    fg="yellow",
    width=25
).pack(pady=10)

tk.Button(
    window,
    text="Train Face Recognizer",
    command=train_model,
    font=("Verdana", 14),
    bg="black",
    fg="yellow",
    width=25
).pack(pady=10)

tk.Button(
    window,
    text="Take Attendance",
    command=take_attendance,
    font=("Verdana", 14),
    bg="black",
    fg="yellow",
    width=25
).pack(pady=10)

tk.Button(
    window,
    text="View Attendance",
    command=view_records,
    font=("Verdana", 14),
    bg="black",
    fg="yellow",
    width=25
).pack(pady=10)

tk.Button(
    window,
    text="Exit",
    command=exit_app,
    font=("Verdana", 14),
    bg="black",
    fg="yellow",
    width=25
).pack(pady=10)

window.mainloop()
