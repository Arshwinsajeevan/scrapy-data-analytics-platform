import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price TEXT,
    availability TEXT,
    rating TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quote TEXT,
    author TEXT,
    tags TEXT
)
""")

conn.commit()
conn.close()

print("Database and tables created successfully.")
