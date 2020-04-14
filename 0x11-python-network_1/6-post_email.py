#!/usr/bin/python3
"""Script to do a POST request to an URL
and print the value passed as parameter into a dictionary
"""
if __name__ == "__main__":
    import sys
    import requests

    data = {}
    data["email"] = sys.argv[2]
    r = requests.post(sys.argv[1], data=data)
    print (r.text)
