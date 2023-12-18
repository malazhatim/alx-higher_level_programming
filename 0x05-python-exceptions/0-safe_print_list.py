#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    for x in range(0, x):
        try:
            print(my_list[x], end="")
            n += 1
        except:
            break
    print("")
    return(n)
