import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("github_token")
url = (f"https://api.github.com/users/")
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}


def get_data(username):
    if not username:
        print("No username entered, please try again")
        return
    response = requests.get(f"{url}{username}", headers=headers)
    repo_response = requests.get(f"{url}{username}/repos",headers=headers)
    if response.status_code==401 or repo_response.status_code==401:
        print("Invalid token/API key")
        return
    if response.status_code==404 or repo_response.status_code==404:
        print("No user found")
        return
    if response.status_code==403 or repo_response.status_code==403 or response.status_code==429 or repo_response.status_code==429:
        print("GitHub API rate limit exceeded. Try again later.")
        return
    data = response.json()
    repo = repo_response.json()
    print(f"""User related data:
    Name:{data.get("name")}
    Usename:{data.get("login")}
    Email:{data.get("email", "Not Public")}
    Location:{data.get("location", "Not Public")}
    Company:{data.get("company", "Not Public")}
    Hireable:{data.get("hireable", "Not Public")}
    Bio:{data.get("bio")}
    Created at:{data.get("created_at")}""")
    print(f"Public Repositories of usename:{data.get("login")}")
    for row in repo:
        print(f"""Repo Name:{row.get("name")}
    Description:{row.get("Description")}
    Folks:{row.get("fork")}
    Size:{row.get("size")}
    Language:{row.get("language")}
    Fork Count:{row.get("forks_count")}
    Created at:{row.get("created_at")}
    Updated at:{row.get("updated_at")}""")

def main():
    username = input("Enter the gitHub username:")
    get_data(username)
    
main()