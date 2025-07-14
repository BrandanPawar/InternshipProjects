import sqlite3

conn = sqlite3.connect("drone_data.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM drone_info")

rows = cursor.fetchall()
columns = [desc[0].strip() for desc in cursor.description]

# Format rows as structured text
lines = []
for row in rows:
    line = " > ".join([str(cell).strip() for cell in row if cell])
    lines.append(line)

# Save to text file
with open("drone_text.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

conn.close()
print("✅ drone_data.db exported to drone_text.txt")
