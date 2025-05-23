# Smart Attendance System using Face Recognition

This is a Face Recognition-based Attendance System built using Python, OpenCV, and SQLite. It allows registering students, training a model using face data, recognizing faces to mark attendance, and viewing stored attendance records — all through a simple GUI.

## 📁 Project Structure

```
dbms project/
├── app_gui.py               # Main GUI application file
├── capture_faces.py         # Script to register new student and capture face images
├── train_faces.py           # Script to train face recognition model
├── recognize_and_mark.py    # Script to detect, recognize and mark attendance
├── view_attendance.py       # Script to view attendance records
├── database.py              # Contains DB schema and DB interaction functions
├── attendance.db            # SQLite database file (auto-generated)
├── dataset/                 # Stores captured face images
├── trainer/                 # Stores trained face recognizer model
├── haarcascade_frontalface_default.xml  # Haar cascade for face detection
└── .gitignore               # Git ignore rules
```

## 🚀 Features

- Add and register students with face capture
- Train face recognizer using LBPH algorithm
- Real-time face recognition and attendance marking
- Store and retrieve attendance using SQLite
- View attendance records from the GUI

## 🛠 Requirements

- Python 3.6+
- OpenCV (`opencv-contrib-python`)
- Pillow
- SQLite3 (comes with Python)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## ▶️ How to Run

1. **Register new student**  
   Run the app and click "Register New Student" to capture face data.

2. **Train the model**  
   Click "Train Face Recognizer" to train the model with captured faces.

3. **Take attendance**  
   Click "Take Attendance" to recognize faces and store attendance records in the DB.

4. **View attendance**  
   Click "View Attendance" to open a window displaying records.

Launch GUI:
```bash
python app_gui.py
```

## 🧠 Database Design

SQLite is used with two tables:

* `students`: stores student ID and name.
* `attendance`: stores timestamped attendance records.

## 📦 GitHub Instructions

To upload this project to GitHub:

```bash
git init
git remote remove origin  # only if origin exists already
git remote add origin https://github.com/YourUsername/YourRepoName.git
git add .
git commit -m "Initial commit"
git push -u origin main  # or master, depending on your branch
```

## 📄 License

This project is built for educational purposes.
