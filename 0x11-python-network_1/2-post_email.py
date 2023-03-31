#!/usr/bin/python3
"""
a script that takes in a URL and an email, 
sends a POST request to the passed URL
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
