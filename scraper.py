import requests
import google.generativeai as genai
import json
import os
from datetime import datetime

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def scrape_jobassam():
    print("Fetching jobassam.in...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    r = requests.get("https://jobassam.in/", headers=headers)
    html = r.text

    prompt = """
    You are scraping https://jobassam.in/. Extract EVERY current job, result, admit card, answer key.

    Return ONLY valid JSON array. No extra text.

    Each object:
    {
      "title": "full title with year",
      "category": "Job or Result or AdmitCard or AnswerKey",
      "department": "department name",
      "postName": "post name or N/A",
      "totalPosts": "number or N/A",
      "lastDate": "date or N/A",
      "applyLink": "url or #",
      "notificationLink": "url or #",
      "description": "short desc"
    }

    HTML: """ + html[:45000]

    response = model.generate_content(prompt)
    text = response.text.strip()
    if text.startswith('['):
        return json.loads(text)
    return []

if __name__ == "__main__":
    jobs = scrape_jobassam()
    print(f"Total jobs: {len(jobs)}")
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)
    print("jobs.json saved")
