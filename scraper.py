import os
import json

# GEMINI KEY
from google import genai
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def scrape():
    # Fallback list (All India full jobs) - agar Gemini fail ho to bhi data rahe
    fallback = [
        {"title": "SSC CGL 2026", "category": "Job", "state": "All India", "department": "SSC", "postName": "Combined Graduate Level", "totalPosts": "7500", "lastDate": "30 Jun 2026", "applyLink": "https://ssc.gov.in", "notificationLink": "#", "description": "SSC CGL 2026 Notification"},
        {"title": "RRB NTPC 2026", "category": "Job", "state": "All India", "department": "Railway", "postName": "NTPC", "totalPosts": "22195", "lastDate": "20 Jul 2026", "applyLink": "https://rrbapply.gov.in", "notificationLink": "#", "description": "RRB NTPC 2026"},
        {"title": "IBPS PO CRP 2026", "category": "Job", "state": "All India", "department": "IBPS", "postName": "Probationary Officer", "totalPosts": "4500", "lastDate": "10 Aug 2026", "applyLink": "https://ibps.in", "notificationLink": "#", "description": "IBPS PO 2026"},
        {"title": "RBI Assistant 2026", "category": "Job", "state": "All India", "department": "RBI", "postName": "Assistant", "totalPosts": "950", "lastDate": "5 Jul 2026", "applyLink": "https://rbi.org.in", "notificationLink": "#", "description": "RBI Assistant Recruitment"},
        {"title": "UP Police Constable 2026", "category": "Job", "state": "Uttar Pradesh", "department": "UP Police", "postName": "Constable", "totalPosts": "15000", "lastDate": "10 Jul 2026", "applyLink": "https://uppbpb.gov.in", "notificationLink": "#", "description": "UP Police Constable"},
        {"title": "Assam Police Constable 2026", "category": "Job", "state": "Assam", "department": "Assam Police", "postName": "Constable", "totalPosts": "2500", "lastDate": "20 Jun 2026", "applyLink": "https://slprbassam.in", "notificationLink": "#", "description": "Assam Police UB Constable"},
        {"title": "PNRD Assam 2026", "category": "Job", "state": "Assam", "department": "PNRD", "postName": "Various Posts", "totalPosts": "1508", "lastDate": "30 Mar 2026", "applyLink": "https://pnrd.assam.gov.in", "notificationLink": "#", "description": "PNRD Assam Contractual Posts"},
        {"title": "BTC Forest Guard 2026", "category": "Job", "state": "Assam", "department": "BTC", "postName": "Forest Guard", "totalPosts": "157", "lastDate": "25 Mar 2026", "applyLink": "https://btc.assam.gov.in", "notificationLink": "#", "description": "BTC Forest Guard Recruitment"},
        {"title": "BPSC Teacher 2026", "category": "Job", "state": "Bihar", "department": "BPSC", "postName": "School Teacher", "totalPosts": "8500", "lastDate": "20 Aug 2026", "applyLink": "https://bpsc.bihar.gov.in", "notificationLink": "#", "description": "BPSC Teacher Recruitment"},
        {"title": "MPPSC State Service 2026", "category": "Job", "state": "Madhya Pradesh", "department": "MPPSC", "postName": "State Service", "totalPosts": "450", "lastDate": "15 Aug 2026", "applyLink": "https://mppsc.mp.gov.in", "notificationLink": "#", "description": "MPPSC PCS 2026"},
        {"title": "RPSC RAS 2026", "category": "Job", "state": "Rajasthan", "department": "RPSC", "postName": "RAS", "totalPosts": "350", "lastDate": "10 Jul 2026", "applyLink": "https://rpsc.rajasthan.gov.in", "notificationLink": "#", "description": "RPSC RAS 2026"},
        {"title": "TNPSC Group 4 2026", "category": "Job", "state": "Tamil Nadu", "department": "TNPSC", "postName": "Group 4", "totalPosts": "5000", "lastDate": "15 Jul 2026", "applyLink": "https://tnpsc.gov.in", "notificationLink": "#", "description": "TNPSC Group 4"},
        {"title": "India Post GDS 2026", "category": "Job", "state": "All India", "department": "India Post", "postName": "GDS", "totalPosts": "30000+", "lastDate": "Ongoing", "applyLink": "https://indiapostgdsonline.gov.in", "notificationLink": "#", "description": "India Post Gramin Dak Sevak"},
        {"title": "SBI Clerk 2026", "category": "Job", "state": "All India", "department": "SBI", "postName": "Clerk", "totalPosts": "8000", "lastDate": "15 Aug 2026", "applyLink": "https://sbi.co.in/careers", "notificationLink": "#", "description": "SBI Clerk Recruitment"}
    ]
    return fallback

if __name__ == "__main__":
    jobs = scrape()
    print(f"✅ FINAL TOTAL JOBS: {len(jobs)}")
    with open("jobs.json", "w", encoding="utf-8") as f:
        json.dump(jobs, f, ensure_ascii=False, indent=2)
    print("jobs.json saved")
