#!/usr/bin/python3
import random
n = random.randint(-10000, 10000)
b = "Last digit of"
a = abs(n) % 10
if n < 0:
    a = -a
    print("{} {} is {} and is less than 6 and not 0".format(b, n, a, end=""))
if a > 5:
    print("{} {} is {} and is greater than 5".format(b, n, a, end=""))
elif a == 0:
    print("{} {} is {} and is 0".format(b, n, a, end=""))
