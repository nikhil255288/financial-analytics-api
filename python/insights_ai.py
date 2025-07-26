import pandas as pd
from sqlalchemy import create_engine

csv_path = r"D:\financial_dashboard_project\data\financial_data.csv"
df = pd.read_csv(csv_path)


# Update these with your actual credentials
db_user = "postgres"         # default user for pgAdmin
db_pass = "Nikhil@0303"
db_host = "localhost"
db_port = "5432"
db_name = "financial_dashboard"

# PostgreSQL connection string
engine = create_engine("""postgresql+psycopg2://postgres:Nikhil%400303@localhost:5432/financial_db""")



# Write to PostgreSQL table
df.to_sql("financial_data", engine, if_exists="replace", index=False)

print("✅ Data loaded into PostgreSQL successfully.")
print(df.head())

print("\n✅ Total Revenue:", df['Revenue'].sum())
print("✅ Total Profit:", df['Profit'].sum())
print("✅ Average Gross Margin (%):", round(df['Gross_Margin_%'].mean(), 2))
print("✅ Top 3 Departments by Revenue:")
print(df.groupby('Department')['Revenue'].sum().sort_values(ascending=False).head(3))