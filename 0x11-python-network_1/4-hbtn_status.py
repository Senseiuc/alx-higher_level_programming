#!/usr/bin/python3
"""
a script that formats html gotten from
a url
"""

if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    html = requests.get(url).text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
