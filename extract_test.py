import pdfplumber

with pdfplumber.open("Designer_.pdf") as pdf:
    full_text = ""
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

# Save text for LLM
with open("wasp3d_text.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("✅ Text extracted to wasp3d_text.txt")
