#!/usr/bin/python3
"""
a script that gets a user tokens
"""
import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, password)).json()

    if 'id' in r:
        print(r['id'])
    else:
        print("None")
