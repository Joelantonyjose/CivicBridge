import sqlite3

conn = sqlite3.connect("civicbridge.db")
cursor= conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    title TEXT,
    description TEXT
)
""")

conn.commit()

conn.close()

print("Database created successfully!")