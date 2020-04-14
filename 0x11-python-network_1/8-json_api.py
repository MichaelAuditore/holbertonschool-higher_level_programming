#!/usr/bin/python3
"""Script to do a POST request to an URL
and print the value passed as parameter into a dictionary
"""
if __name__ == "__main__":
    import sys
    import requests

    data = {}
    if (len(sys.argv) > 1):
        data["q"] = sys.argv[1]
    else:
        data["q"] = ""
    r = requests.post(sys.argv[1], data=data)
    try:
        json = r.json()
        if (len(js) == 0):
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except:
        print("Not a valid JSON")
