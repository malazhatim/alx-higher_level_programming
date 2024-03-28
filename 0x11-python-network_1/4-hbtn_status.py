#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status0000."""

if __name__ == '__main__':
    import requests
    URL = requests.get('https://intranet.hbtn.io/status')
    print("Body response:$")
    print("\t- type: {}$".format(URL.text.__class__))
    print("\t- content: {}$".format(URL.text))
