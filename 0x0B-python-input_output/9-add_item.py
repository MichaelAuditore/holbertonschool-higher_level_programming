#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and
then save into a file
"""
import sys
import os

save_to_json = __import__('7-save_to_json_file').save_to_json_file
load_from = __import__('8-load_from_json_file').load_from_json_file

if os.path.isfile("add_item.json"):
    lst = load_from("add_item.json")
else:
    lst = []

for idx in range(1, len(sys.argv)):
    lst.append(sys.argv[idx])
save_to_json(lst, "add_item.json")
