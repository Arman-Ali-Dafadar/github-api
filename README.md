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
<pre>bash git clone https://github.com/Arman-Ali-Dafadar/github-api.git
cd github-api</pre>

2. Install Dependencies
<pre>bash pip install -r requirements.txt</pre>


## GitHub API Token Setup
1. Go to GitHub → Settings → Developer settings
2. Open Personal access tokens
3. Generate a token (classic or fine-grained)
4. No special scopes are required for public data
5. Create a .env file in the repository root directory
6. Copy the token to the .env file as `github_token=paste your personal access token here`
