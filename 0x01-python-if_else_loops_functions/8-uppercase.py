#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            w = chr(ord(i)-32)
        else:
            w = i
        print("{}".format(w), end='')
    print('{}'.format(''))
