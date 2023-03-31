#!/usr/bin/python3
"""
a script that takes in a URL and an email,
sends a POST request to the passed URL
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    r = requests.post(url, value)
    print(r.text)
