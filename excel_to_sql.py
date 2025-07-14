import pandas as pd
import sqlite3

# Load CSV
df = pd.read_csv("data.csv")

# Connect to SQLite DB (creates file if not exists)
conn = sqlite3.connect("products.db")

# Write the data into a table named 'products'
df.to_sql("products", conn, if_exists="replace", index=False)

conn.close()
print("✅ CSV data inserted into products.db (table: products)")
