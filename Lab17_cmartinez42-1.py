"""
Program Name: Hacker News Article Fetcher
Author: Chris Martinez
Purpose: Gets popular articles from Hacker News and prints them without crashing if comments are missing.
Starter Code:'hn_submissions.py' from Chapter 17
Date: 8/10/2026
"""

import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()

for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    title = response_dict.get("title", "No Title")
    comments = response_dict.get("descendants", 0)

    print(f"\nTitle: {title}")
    print(f"Discussion Link: http://news.ycombinator.com/item?id={submission_id}")
    print(f"Comments: {comments}")


