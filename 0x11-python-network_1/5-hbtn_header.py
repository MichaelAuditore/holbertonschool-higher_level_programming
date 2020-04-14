#!/usr/bin/python3
"""Script to do a request to an URL and get value of variable
X-Request-Id using requests module
"""
if __name__ == "__main__":
    import requests

    req = requests.get("https://intranet.hbtn.io/status")
    headers = req.headers
    for header, value in headers.items():
        if (header == "X-Request-Id"):
            print(value)
