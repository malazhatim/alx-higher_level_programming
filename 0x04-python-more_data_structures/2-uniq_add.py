#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    uniq = list(set(my_list))
    for i in uniq:
        a += i
    return (a)
