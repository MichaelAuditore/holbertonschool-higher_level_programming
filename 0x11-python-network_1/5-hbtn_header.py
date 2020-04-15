#!/usr/bin/python3
"""Script to do a request to an URL and get value of variable
X-Request-Id using requests module
"""
if __name__ == "__main__":
    import requests
    import sys

    req = requests.get(sys.argv[1])
    headers = req.__dict__.get("headers")
    id = headers.get("x-request-id")
    print(id)
