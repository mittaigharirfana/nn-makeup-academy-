import requests
import json

response = requests.get("http://localhost:8001/api/courses")
courses = response.json()

# Find a small course
for course in courses:
    if course['title'] == "Basic Eyebrow Shaping & Enhancement":
        print(json.dumps(course, indent=2))
        break
