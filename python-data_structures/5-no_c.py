#!/usr/bin/python3

def no_c(my_string):
    i = {ord('C'): None, ord('c'): None}
    result = my_string.translate(i)
    print(result)
    return result
