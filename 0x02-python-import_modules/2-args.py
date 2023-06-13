#!/usr/bin/python3

if __name__ == "__main__":

    import sys


    count = len(sys.argv) - 1

    if count == 0:
        print("{} arguments.".format(count))
    if count == 1:
        print("{} argument:".format(count))


    if count > 1:
        print("{} arguments:".format(count))
        count = 0
        for arg in sys.argv:
            if count != 0:
                print("{}: {}".format(count, arg))
            count = count + 1
