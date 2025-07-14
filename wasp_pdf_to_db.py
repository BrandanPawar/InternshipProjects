import pdfplumber
import sqlite3

# Step 1: Load your PDF
with pdfplumber.open("Designer_.pdf") as pdf:
    full_text = ""
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

# Step 2: Save to SQLite
conn = sqlite3.connect("wasp3d_info.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS wasp_info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT
)
""")

cursor.execute("INSERT INTO wasp_info (content) VALUES (?)", (full_text,))
conn.commit()
conn.close()

print("✅ PDF data stored in wasp3d_info.db")
