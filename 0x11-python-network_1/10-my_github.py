#!/usr/bin/python3
"""Script to do a POST request to github api to get an specific user
connecting with a basic auth using username and password and print id
"""
if __name__ == "__main__":
    import sys
    import requests
    user = sys.argv[1]
    pwd = sys.argv[2]
    url = "https://api.github.com/users"
    url = url + "/{}".format(user)
    r = requests.get(url, auth=requests.auth.HTTPBasicAuth(user, pwd))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print("None")
