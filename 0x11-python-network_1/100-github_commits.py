#!/usr/bin/python3
"""Script to do a POST request to github api to get an specific info about
a repo in this case print the latest 10 commits
"""
if __name__ == "__main__":
    import sys
    import requests

    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
    r = requests.get(url)
    ncommits = 0
    for line in r.json():
        if (ncommits < 10):
            commit = r.json()[ncommits]
            sha = commit.get("sha")
            author = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
        ncommits += 1
