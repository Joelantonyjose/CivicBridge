import sqlite3

conn = sqlite3.connect("civicbridge.db")

cursor = conn.cursor()

cursor.execute(
    "ALTER TABLE reports ADD COLUMN username TEXT"
)

conn.commit()

conn.close()

print("Username column added successfully")