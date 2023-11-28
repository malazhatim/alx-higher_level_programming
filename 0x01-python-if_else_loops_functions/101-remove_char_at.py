#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ''
    if n > len(str) or n < 0:
        return str
    for a in str:
        if a != str[n]:
            str2 += a
    return str2
