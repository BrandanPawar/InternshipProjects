import subprocess

# Load extracted PDF content
with open("wasp3d_text.txt", "r", encoding="utf-8") as f:
    context = f.read()

question = input("Ask me anything about the PDF: ")

prompt = f"""
You are an assistant. Based on the document below, answer the question.

DOCUMENT:
\"\"\"
{context}
\"\"\"

QUESTION:
{question}

ANSWER:
"""

# Use UTF-8 encoded input to avoid Windows encoding errors
result = subprocess.run(
    ["ollama", "run", "mistral"],
    input=prompt.encode('utf-8'),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

# Decode output as UTF-8
print(result.stdout.decode('utf-8'))
