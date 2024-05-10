#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        letter = ord(char)
        if 97 <= letter <= 122:
            upper += chr(letter - 32)
        else:
            upper += char
        print("{}".format(upper))
