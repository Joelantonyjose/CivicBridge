import sqlite3

conn = sqlite3.connect("civicbridge.db")
cursor = conn.cursor()

cursor.execute(
    "ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'Citizen'"
)

conn.commit()
conn.close()

print("Role column added successfully")