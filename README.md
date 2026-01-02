# Github Profile CLI Tool

## Overview
A command-line tool that fetches and displays public GitHub user information using the GitHub REST API.
It uses token-based authentication, handles common API errors, and presents clean, readable output in the terminal.

This tool is useful for quickly inspecting GitHub profiles without opening a browser.

## Features
- Fetch GitHub user profile details(the ones which are public):
    - Username
    - Name
    - Bio
    - Location
    - Company
    - Email
    - Hireable status

- Token-based authentication using environment variables (.env file used)

- Simple error handling:
    - User not found (404)
    - Invalid or missing token (401)
    - API rate limits (403 or 429)

- Simple CLI interface

## Setup
1. Clone the repository
<pre>git clone https://github.com/Arman-Ali-Dafadar/github-api.git
cd github-api</pre>

2. Create a virtual environment(optional but highly recommended)
<pre>python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
</pre>
3. Install Dependencies
<pre>pip install -r requirements.txt</pre>


## GitHub API Token Setup
1. Go to GitHub → Settings → Developer settings
2. Open Personal access tokens
3. Generate a token (classic or fine-grained)
4. No special scopes are required for public data
5. Create a .env file in the repository root directory
6. Copy the token to the .env file as `github_token=paste your personal access token here`

## Usage
Simply run the python file using:
<pre>python3 app.py</pre>
And enter the desired GitHib username when prompted.

Sample Example:
<pre>
Enter the gitHub username:torvalds
User related data:
    Name:Linus Torvalds
    Usename:torvalds
    Email:None
    Location:Portland, OR
    Company:Linux Foundation
    Hireable:None
    Bio:None
    Created at:2011-09-03T15:26:22Z
Public Repositories of usename:torvalds
Repo Name:linux
    Description:None
    Folks:False
    Size:5899100
    Language:C
    Fork Count:59703
    Created at:2011-09-04T22:48:12Z
    Updated at:2026-01-02T20:00:50Z
</pre>
> The shown output is just for an example.

## Limitations
- Only public GitHub data is accessible
- Private repositories and emails are not visible
- Rate limits depend on GitHub API policies