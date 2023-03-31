#!/usr/bin/python3
"""
a script that displays the value of the X-Request-Id
a url given as an argument
"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info()
print(html.get("X-Request-Id"))
