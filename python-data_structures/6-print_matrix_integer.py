#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        #range i for print vertical line
        for j in range(len(matrix[i])):
            #range j for print horizontal line
            if j != 0:
                print(" ", end="")
            print("{:d}".format(matrix[i][j]), end="")
        print()
