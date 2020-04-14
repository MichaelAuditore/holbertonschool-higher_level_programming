#!/usr/bin/python3
"""Script to send a request to an URL and get the value of header
X-Request-Id
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.getheaders()
        for header in html:
            if (header[0] == 'X-Request-Id'):
                print(header[1])
