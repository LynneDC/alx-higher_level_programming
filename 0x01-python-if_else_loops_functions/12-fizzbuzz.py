#!/usr/bin/python3
str1 = "Fizz "
str2 = "Buzz "
str3 = "FizzBuzz "
def fizzbuzz():
    for num in range(1, 100):
#    print("{}".format(num))
        if num % 3 == 0 and num % 5 == 0:
            print("{}".format(str3), end="")
        elif num % 3 == 0:
            print("{}".format(str1), end="")
        elif num % 5 == 0:
            print("{}".format(str2), end="")
        else:
            print("{} ".format(num), end="")
