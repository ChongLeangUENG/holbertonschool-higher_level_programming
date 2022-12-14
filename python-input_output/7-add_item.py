#!/usr/bin/python3
"""JSON String function"""


from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file = "add_item.json"

try:
    list = load_from_json_file(file)
except Exception:
    list = []

for arg in argv[1:]:
    list.append(arg)

save_to_json_file(list, file)
