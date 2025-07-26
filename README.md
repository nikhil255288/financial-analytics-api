## 📊 Power BI Dashboard

A snapshot of the Power BI dashboard used in this project:

![Power BI Dashboard](screenshots/powerbi_dashboard.png)



# 💸 Financial Analytics API & Power BI Dashboard

A simple yet powerful Financial Analytics web API built using **FastAPI**, backed by a structured SQLite database. The project provides an interface to access financial KPIs and visualize company data using **Power BI**.

---

## 🚀 Features

- 🔍 Filter financial data by company and year
- ⚡ Fast and lightweight API using FastAPI
- 📂 SQLite-backed persistent storage
- 📊 Integrated with Power BI for interactive visualizations
- 🔁 Easily extendable for more companies or metrics

---

## 📁 Project Structure

financial_dashboard_project/
├── main.py # FastAPI server
├── init_db.py # DB schema & sample data
├── database.py # DB connection logic
├── models.py # Pydantic models
├── screenshots/ # Contains dashboard images
└── README.md # This file


# Initialize database
python init_db.py

# Start the FastAPI server
python -m uvicorn main:app --reload

Author
🙌 Author  
Made with 💙 by [Nikhil](https://www.linkedin.com/in/nikhil-teja-b00ab1282/)

