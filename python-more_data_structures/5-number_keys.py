#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    list_key = list(a_dictionary.keys())

    for i in list_key:
        count = count + 1

    return count
