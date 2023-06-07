#!/usr/bin/python3

for num in range(10):
    for num1 in range(1, 10):
        if num < num1:
            continue
        if num == 9 and num1 == 8:
            print("{}{}".format(num, num1))
            break
        if num != num1:
            print("{:02d} {:02d}".format(num, num1), end=" ")
