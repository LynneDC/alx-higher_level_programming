#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
st = "Last digit of"
d = abs(number) % 10
if number < 0:
    d = -d
    print(f"{st} {number} is {d} and is less than 6 and not 0")
if d > 5:
    print(f"{st} {number} is {d} and is greater than 5")
elif d == 0:
    print(f"{st} {number} is {d} and is 0")
