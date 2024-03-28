#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""

if __name__ == '__main__':
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    try:
        a = sys.argv[1]
    except Exception:
        a = ""
    s = {"q": a}
    req = requests.post(url, data=s)
    try:
        result = req.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")
