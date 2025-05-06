# init_db.py

import sqlite3

def initialize_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()

    # Create students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            registered_on TEXT NOT NULL
        )
    """)

    # Create attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_db()
