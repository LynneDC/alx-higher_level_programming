#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = "Last digit of"
d = abs(number) % 10
if number < 0:
    d = -d
    print("{} {} is {} and is less than 6 and not 0".format(st, number, d, end=""))
if d > 5:
    print("{} {} is {} and is greater than 5".format(st, number, d, end=""))
elif d == 0:
    print("{} {} is {} and is 0".format(st, number, d, end=""))
