#!/usr/bin/python3

import sys


def print_args():
    count = len(sys.argv) - 1
    args = "arguments" if (count > 1 or count == 0) else "argument"

#    print("{} {}: ".format(count, args))

    if count == 0:
        print("{} {}:".format(count, args))
    if count > 0:
        print("{} {}: ".format(count, args))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    print_args()
