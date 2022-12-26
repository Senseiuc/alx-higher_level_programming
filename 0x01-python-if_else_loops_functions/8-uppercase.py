#!/usr/bin/python3
def uppercase(str):
    for (j, i) in enumerate(str):
        if ord(i) > 96 and ord(i) < 123:
            str = str.replace(str[j], chr(ord(i)-32))
    print(str)
