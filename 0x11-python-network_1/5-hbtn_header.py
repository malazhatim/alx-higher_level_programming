#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""

if __name__ == '__main__':
    import requests
    import sys
    request = requests.get(sys.argv[1])
    print(request.headers.get('X-Request-Id'))
