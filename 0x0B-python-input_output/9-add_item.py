#!/usr/bin/python3
import sys
import os
save_to_json = __import__('7-save_to_json_file').save_to_json_file
load_from = __import__('8-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json") is True:
    lst = list(load_from("add_item.json"))
    for idx in range(len(sys.argv)):
        if idx == 0:
            continue
        lst.append(sys.argv[idx])
        save_to_json(lst, "add_item.json")
else:
    lst = []
    save_to_json(lst, "add_item.json")
