#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    for i in a.keys():
        a[i] = a[i] * 2
    return a
