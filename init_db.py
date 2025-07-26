import sqlite3
import pandas as pd

# Connect to SQLite DB (it will create test.db if it doesn't exist)
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Create financial_data table
cursor.execute('''
CREATE TABLE IF NOT EXISTS financial_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    revenue REAL,
    expenses REAL,
    profit REAL,
    year INTEGER
)
''')

# Insert dummy data
dummy_data = [
    ("Apple", 300000, 200000, 100000, 2023),
    ("Google", 250000, 150000, 100000, 2023),
    ("Amazon", 400000, 300000, 100000, 2023),
    ("Tesla", 150000, 100000, 50000, 2023),
    ("Microsoft", 350000, 250000, 100000, 2023)
]

cursor.executemany('''
INSERT INTO financial_data (company, revenue, expenses, profit, year)
VALUES (?, ?, ?, ?, ?)
''', dummy_data)

# Save and close
conn.commit()
conn.close()

print("✅ Database initialized with dummy data.")
