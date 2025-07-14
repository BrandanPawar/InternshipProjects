import requests
import json
import re

def ask_llm(user_input):
    url = "http://localhost:11434/api/generate"
    prompt = f"""
You are an intelligent assistant for a live media control system. When given a user message,
perform two things:
1. Summarize the news content if present.
2. Extract and interpret any media control command (like switch camera, start ticker, etc.)
Return the result in a JSON format as:
{{
  "summary": "<summary_text>",
  "command": "<parsed_command>",
  "target": "<camera/ticker/graphic/etc>"
}}

User input: {user_input}
"""

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    raw_output = response.json()["response"]

    # Try to extract JSON using regex
    try:
        json_text = re.search(r"\{.*\}", raw_output, re.DOTALL).group(0)
        parsed = json.loads(json_text)
    except Exception as e:
        parsed = {
            "summary": "Could not parse summary.",
            "command": "unknown",
            "target": ""
        }

    return parsed