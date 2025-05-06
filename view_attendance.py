# view_attendance.py

import sqlite3
import pandas as pd

def view_attendance():
    conn = sqlite3.connect("attendance.db")
    query = """
        SELECT a.id, s.name, a.date, a.time
        FROM attendance a
        JOIN students s ON a.student_id = s.id
        ORDER BY a.date DESC, a.time DESC
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    if df.empty:
        print("[INFO] No attendance records found.")
    else:
        print("\n[ATTENDANCE RECORDS]")
        print(df.to_string(index=False))

if __name__ == "__main__":
    view_attendance()
