#!/usr/bin/python3
# function that convert every lowercase to upper case

def uppercase(str):
    uppecase = ""
    for a in str:
        if ord("a") <= ord(a) <= ord("z"):
            uppecase += chr(ord(a) - 32)
        else:
            uppecase += a
    print("{}".format(uppecase))
