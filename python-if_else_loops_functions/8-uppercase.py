#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        letter = ord(char)
        if 97 <= letter <= 122:
            char = chr(letter - 32)
        upper += char
    print("{}".format(upper))
