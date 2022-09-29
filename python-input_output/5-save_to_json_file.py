#!/usr/bin/python3
"""JSON string"""
import json


def save_to_json_file(my_obj, filename):
    """save object in json
        Args:
            my_obj: Object
            filename: String file   
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)