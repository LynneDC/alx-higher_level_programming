#!/usr/bin/python3

def remove_char_at(string, n):
    str1 = ""
    for i in range(len(string)):
        if i != n:
            str1 = str1 + string[i]
    return str1
