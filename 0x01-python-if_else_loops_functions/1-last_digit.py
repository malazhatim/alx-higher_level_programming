#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    a = - 1 * (-number % 10)
else:
    a = number % 10

if a > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, a))
elif a == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, a))
elif a < 6 and a != 0:
    print("Last digit of {:d} is {:d}".format(number, a), end=" ")
    print("and is less than 6 and not 0")
