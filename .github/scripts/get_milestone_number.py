import os
import requests
import sys

title = sys.argv[1] # Milestone title

repo = os.environ['GITHUB_REPOSITORY'] # As in, user/repo

print( f"Fetching number of milestone '{title}' of repo '{repo}'", file = sys.stderr )

url = f'https://api.github.com/repos/{repo}/milestones'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}

page = 1
number = None
while number is None:

    params = {
        'sort': 'due_on',
        'direction': 'asc',
        'per_page': 100,
        'page': page
    }

    r = requests.get( url, headers = headers, params = params )
    if r.status_code != 200:
        raise Exception( f"HTTP request failed: code {r.status_code}" )
    r = r.json()

    if not r: # Empty page
        raise Exception( "Milestone not found" )
    page += 1

    for milestone in r:
        if milestone['title'] == title:
            number = milestone['number']
            print( f"Milestone number: {number}", file = sys.stderr )

print( number )