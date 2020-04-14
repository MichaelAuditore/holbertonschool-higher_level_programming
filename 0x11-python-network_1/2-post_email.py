#!/usr/bin/python3
"""Script to do a POST request to an URL
and print the value passed as parameter into a JSON
"""
if __name__ == "__main__":
    import sys
    import urllib.request

    var = {'email': '{}'.format(sys.argv[2])}
    enc_data = urllib.parse.urlencode(var)
    enc_data = enc_data.encode('ascii')
    try:
        with urllib.request.urlopen(sys.argv[1], data) as response:
            for i in response:
                print(i.decode('utf-8'))
    except urllib.error.URLError as e:
        # In case of URL failed conection or refused
        print(e.reason)
