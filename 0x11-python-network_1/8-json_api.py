#!/usr/bin/python3
"""Script to do a POST request to an URL
and print the value passed as parameter into a dictionary
"""
if __name__ == "__main__":
    import sys
    import requests

    send = {'q': ""}
    if (len(sys.argv) > 1):
        send['q'] = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data=send)
    try:
        json = r.json()
        if (len(json) == 0):
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except:
        print("Not a valid JSON")
