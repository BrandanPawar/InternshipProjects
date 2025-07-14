import sqlite3

def search_topic(query):
    conn = sqlite3.connect("drone_data.db")
    cursor = conn.cursor()

    # Search in all levels using LIKE
    cursor.execute("""
        SELECT * FROM drone_info
        WHERE
            "Level 1" LIKE ? OR
            "Level 2 " LIKE ? OR
            "Level 3" LIKE ? OR
            "Level 4 " LIKE ? OR
            "Level 5" LIKE ? OR
            "Level 6" LIKE ?
    """, tuple([f"%{query}%"] * 6))

    rows = cursor.fetchall()
    conn.close()

    if rows:
        result = ""
        for row in rows:
            row_text = " > ".join([col for col in row if col and col.strip()])
            result += f"• {row_text}\n"
        return result
    else:
        return "No matching topic found."

# CLI Loop
while True:
    question = input("Ask a topic from the drone guide (type 'exit' to quit): ")
    if question.lower() == "exit":
        break
    print(search_topic(question))
