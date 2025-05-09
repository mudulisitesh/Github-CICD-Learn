# generate_dsa_problem.py
import os
import requests
import json

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

PROMPT = "Write a random DSA (Data Structures and Algorithms) problem and provide a working code solution in Python."

def call_gemini(prompt):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    
    try:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return "Invalid response from Gemini API."

if __name__ == "__main__":
    result = call_gemini(PROMPT)
    with open("dsa_solution.py", "w") as f:
        f.write(result)
