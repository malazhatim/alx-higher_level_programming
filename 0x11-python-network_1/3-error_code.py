#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./3-error_code.py <URL>
  - Handles HTTP errors.
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            info = response.read()
            print(info.decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
