#!/usr/bin/python3

<<<<<<< HEAD
for num in range(10):
    for num1 in range(1, 10):
        if num < num1:
            continue
        if num == 9 and num1 == 8:
           print("{}{}".format(num, num1))
           break
        if num != num1:
           print("{:02d} {:02d}".format(num, num1), end=" ")
=======
for i in range(10):
    for j in range(i, 10):
        if i != j:
            print("{:02d}, {:02d}".format(i, j), end=", ")
print()

>>>>>>> 2c2e4989332b8c75017d1cee3ee811673c670120
