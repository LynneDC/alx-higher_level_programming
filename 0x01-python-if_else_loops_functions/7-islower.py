#!/usr/bin/python3
#function that check if letter entered is lower

def islower(c):
    for a in range(97, 123):
        if ord(c) != a:
            return False
        else:
            return True
