from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import pandas as pd

app = FastAPI()

# ------------------------ CORS Middleware ------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------ Create Table if Not Exists ------------------------
def create_table_if_not_exists():
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS financial_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            revenue REAL,
            profit REAL,
            expenses REAL,
            year INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# ------------------------ OPTIONAL: Insert One Dummy Row ------------------------
def seed_data():
    conn = sqlite3.connect('financial_data.db')
    cursor = conn.cursor()

    # Check if table already has data
    cursor.execute("SELECT COUNT(*) FROM financial_data")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute('''
            INSERT INTO financial_data (company, revenue, profit, expenses, year)
            VALUES (?, ?, ?, ?, ?)
        ''', ('Apple', 500.0, 120.0, 300.0, 2022))
        conn.commit()
    
    conn.close()

# Call these once at startup
create_table_if_not_exists()
seed_data()

# ------------------------ Routes ------------------------
@app.get("/")
def read_root():
    return {"msg": "Backend is working!"}

@app.get("/data")
def get_data(company: str = Query(None), year: int = Query(None)):
    try:
        conn = sqlite3.connect("financial_data.db")
        query = "SELECT * FROM financial_data"
        conditions = []

        if company:
            conditions.append(f"company = '{company}'")
        if year:
            conditions.append(f"year = {year}")
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        query += " LIMIT 100"

        df = pd.read_sql_query(query, conn)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": str(e)}
