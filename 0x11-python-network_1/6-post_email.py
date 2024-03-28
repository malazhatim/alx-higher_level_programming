#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys
    em = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=em)
    print(req.text)
