# app.py

from flask import Flask, render_template, request, redirect, url_for
import capture_faces
import train_faces
import recognize_and_mark
import view_attendance

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_student():
    capture_faces.register_student()
    return redirect(url_for('home'))

@app.route('/train', methods=['POST'])
def train_model():
    train_faces.train_model()
    return redirect(url_for('home'))

@app.route('/attendance', methods=['POST'])
def take_attendance():
    recognize_and_mark.recognize_and_mark_attendance()
    return redirect(url_for('home'))

@app.route('/view', methods=['POST'])
def view_records():
    view_attendance.view_attendance()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
