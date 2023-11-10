#!/usr/bin/python3
"""
adds and saves to Python object to JSON file; loads objects
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    existing = load_from_json_file('add_item.json')
except FileNotFoundError:
    existing = []

save_to_json_file(existing + argv[1:], 'add_item.json')
