import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('attendance.db')  # Replace with your database file path
cursor = conn.cursor()

# Query to view all records from a table (e.g., students table)
cursor.execute("SELECT * FROM students")  # Replace 'students' with your table name

# Fetch all results
rows = cursor.fetchall()

# Display the rows
for row in rows:
    print(row)

# Close the connection
conn.close()
