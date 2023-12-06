#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    r = ""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > a:
                r = k
                a = v
        return r
    else:
        return None
