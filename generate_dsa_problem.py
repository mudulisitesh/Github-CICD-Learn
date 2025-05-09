# generate_dsa_problem.py
import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=GEMINI_API_KEY"  # Replace with actual endpoint

PROMPT = "Write a random DSA (Data Structures and Algorithms) problem and provide a working code solution in Python."

def call_gemini(prompt):
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "prompt": prompt
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response.json().get("text", "No output")

if __name__ == "__main__":
    result = call_gemini(PROMPT)
    with open("dsa_solution.py", "w") as f:
        f.write(result)
