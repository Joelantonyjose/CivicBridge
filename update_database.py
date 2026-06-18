import sqlite3

conn=sqlite3.connect("civicbridge.db")
cursor=conn.cursor()

cursor.execute(
    "ALTER TABLE reports ADD COLUMN status TEXT"
)

conn.commit()
conn.close()

print("Status column added successfully")