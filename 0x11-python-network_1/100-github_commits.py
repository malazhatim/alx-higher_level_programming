#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
Usage: ./100-github_commits.py <repository name> <repository owner>
"""

if __name__ == '__main__':
    import sys
    import requests
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    repo_info = owner_name + "/" + repo_name
    url = "https://api.github.com/repos/" + repo_info + "/commits"
    req = requests.get(url)
    x = req.json()[:10]
    for a in x:
        b = a['sha']
        author = a['commit']['author']['name']
        print('{}: {}'.format(b, author))
