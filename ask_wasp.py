import sqlite3

def ask_question(query):
    conn = sqlite3.connect("wasp3d_info.db")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM wasp_info")
    data = cursor.fetchone()
    conn.close()

    if not data:
        return "No data found in the database."

    content = data[0].lower()
    query = query.lower()

    if "wasp3d" in query:
        start = content.find("wasp3d")
        return content[start:start+800].strip()

    elif "Render Statistics" in query or "Render" in query:
        start = content.find("Render Statistics")
        if start == -1:
            start = content.find("Render")
        return content[start:start+800].strip() if start != -1 else "Render statistics section not found."

    elif "graphics" in query:
        start = content.find("graphics")
        return content[start:start+800].strip() if start != -1 else "Graphics section not found."

    else:
        return "Sorry, I don't understand that question."

# Main loop
while True:
    user_input = input("Ask something (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    print(ask_question(user_input))
