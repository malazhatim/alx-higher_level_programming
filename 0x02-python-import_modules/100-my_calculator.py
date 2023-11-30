#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    opration = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(oprations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    i = int(sys.argv[1])
    j = int(sys.argv[3])
    print("{} {} {} = {}".format(i, sys.argv[2], j, oprationss[sys.argv[2]](i, j)))
