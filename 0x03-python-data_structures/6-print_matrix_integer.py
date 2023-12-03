#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    l = len(matrix)
    for a in range(l):
        for b in range(len(matrix[a])):
            print('{:d}'.format(matrix[a][b]), end='')
            if b is not (len(matrix[a]) - 1):
                print(end=" ")
        print("")
