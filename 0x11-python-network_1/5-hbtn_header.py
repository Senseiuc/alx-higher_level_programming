#!/usr/bin/python3
"""
a script that displays the value of the X-Request-Id
a url given as an argument
"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
