#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of "
last_digit = number[-1:]

if last_digit > 5:
    print(str.format(number, last_digit) "and is greater than 5")
    """
if last_digit == 0:
    print(str"{} is" last_digit "and is 0".format(number))
if last_digit < 6 and last_digit != 0:
    print(str"{} is" last_digit "and is less than 6 and not 0".format(number))
  """ 
