#!/usr/bin/python3
"""
a script that takes in a URL and an email,
sends a POST request to the passed URL
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''
    value = {'q': q}
    try:
        r = requests.post(url, value).json()
        if 'id' in r and 'name' in r:
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
