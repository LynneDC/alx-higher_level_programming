#!/usr/bin/python3
for num1 in range(9):
    for num2 in range(1, 10):
        if num2 < num1:
            continue
        if num2 == 9 and num1 == 8:
            print(f"{num1}{num2}")
            break
        if num1 != num2:
            print(f"{num1}{num2}, ", end="")
