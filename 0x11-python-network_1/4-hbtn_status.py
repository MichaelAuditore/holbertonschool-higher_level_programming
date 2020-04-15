#!/usr/bin/python3
"""Script to do a request to an URL and print body
 response using requests module
"""
if __name__ == "__main__":
    import requests

    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}".format(
        type(req.text), req.text))
