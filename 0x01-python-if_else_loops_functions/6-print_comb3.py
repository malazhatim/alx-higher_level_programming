#!/usr/bin/python3
a = 1
for b in range(9):
    for c in range(a, 10):
        if a != 9:
            print('{:d}{:d}, '.format(b, c), end="")
        else:
            print('{:d}{:d}'.format(b, c))
    a += 1
