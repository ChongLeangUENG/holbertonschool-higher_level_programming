#!/usr/bin/python3

def element_at(my_list, idx):
    if 0 >= idx and idx <= len(my_list):
        return None
    return my_list[idx]