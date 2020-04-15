#!/usr/bin/python3
"""Script to do a POST request to an URL
and print the value passed as parameter into a dictionary
"""
if __name__ == "__main__":
    import sys
    import requests

    data = {'q': ""}
    if (len(sys.argv) > 1):
        data['q'] = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json = r.json()
        if (len(js) == 0):
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except:
        print("Not a valid JSON")
