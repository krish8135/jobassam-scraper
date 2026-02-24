import os
import requests
from google import genai
import json

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def scrape():
    print("Fetching https://assamcareer.com/ ...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    r = requests.get("https://assamcareer.com/", headers=headers)
    html = r.text

    prompt = """
You are scraping https://assamcareer.com/ - Assam govt jobs site.

Extract ALL current job notifications.

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
  "description": "short description"
}

Extract as many as possible.

HTML: """ + html[:50000]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    text = response.text.strip()

    if text.startswith('['):
        return json.loads(text)
    return []

if __name__ == "__main__":
    jobs = scrape()
    print(f"Total jobs: {len(jobs)}")
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)
    print("jobs.json saved")
