import subprocess

# Load the drone text content
with open("drone_text.txt", "r", encoding="utf-8") as f:
    context = f.read()

question = input("Ask your question about the Drone Designer manual:\n> ")

prompt = f"""
You are a helpful assistant answering questions from a technical drone software manual.

DOCUMENT:
\"\"\"
{context}
\"\"\"

QUESTION:
{question}

ANSWER:
"""

# Use Ollama to answer (uses 'mistral' by default — you can change it)
result = subprocess.run(
    ["ollama", "run", "mistral"],
    input=prompt.encode("utf-8"),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("\n🧠 Answer from Ollama:\n")
print(result.stdout.decode("utf-8"))
