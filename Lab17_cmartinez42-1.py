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




