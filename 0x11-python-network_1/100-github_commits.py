#!/usr/bin/python3
"""
a script that gets a user tokens
"""
import requests
from sys import argv

if __name__ == "__main__":
    REPO = argv[1]
    OWNER = argv[2]
    url = "https://api.github.com/repos/" + OWNER + "/" + REPO + "/commits"

    r = requests.get(url).json()
    for i in r[:10]:
        print("{}: {}".format(i['commit']['author']['name'], i['sha']))
