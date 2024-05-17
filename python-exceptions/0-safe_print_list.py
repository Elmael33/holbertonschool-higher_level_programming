#!/usr/bin/python3

def safe_print_list(my_list=[], count=0):
    try:
        for i in range(count):
            print(my_list[i], end="")
    except IndexError:
        count = i
    finally:
        print()
        return count
    