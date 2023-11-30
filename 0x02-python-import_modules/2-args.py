#!/usr/bin/python3
if __name__ == "__main__":
    import sys
def main(*argv):
    a = 0
    l = len(sys.argv) - 1
    if l == 1:
        print("{:d} argument:".format(l))
    elif l == 0:
        print("{:d} arguments.".format(l))
    else:
        print("{:d} arguments:".format(l))
    for args in sys.argv:
        if (a != 0):
            print("{}: {}".format(a, args))
        a += 1
