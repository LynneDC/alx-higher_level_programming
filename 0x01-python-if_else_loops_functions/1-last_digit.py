#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
digit = abs(number) % 10
if number < 0:
    digit = -digit
    print("{} {} is {} and is less than 6 and not 0".format(string, number, digit, end=""))
if digit > 5:
    print("{} {} is {} and is greater than 5".format(string, number, digit, end=""))
elif digit == 0:
    print("{} {} is {} and is 0".format(string, number, digit, end=""))
#if number < 0:
#    digit = -digit
#   print("{} {} is {} and is less than 6 and not 0".format(string, number,  digit, end=""))
