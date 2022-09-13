#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    biggest = my_list[0]

    for number in range(1, len(my_list)):
        if my_list[number] > biggest:
            biggest = my_list[number]

    return biggest
