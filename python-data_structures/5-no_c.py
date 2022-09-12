#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for rm in my_string:
        if rm != 'c' and rm != 'C':
            new += rm
    return new 
