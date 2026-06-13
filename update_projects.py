import requests
import json

USERNAME = "josweenaj-byte"

url = f"https://api.github.com/users/{USERNAME}/repos"

repos = requests.get(url).json()

projects = []

for repo in repos:
    if not repo["fork"]:
        projects.append({
            "name": repo["name"],
            "description": repo["description"],
            "url": repo["html_url"],
            "language": repo["language"]
        })

with open("projects.json", "w") as f:
    json.dump(projects, f, indent=2)
