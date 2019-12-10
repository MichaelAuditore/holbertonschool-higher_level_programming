#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print("{:c}".format(
            (ord(i) - 32) if i >= 'a' and i <= 'z' else ord(i)
        ), end="")
    else:
        print("")
