#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nel = 0
    if my_list:
        for i in range(0, x):
            try:
                print("{}".format(my_list[i]), end="")
            except IndexError:
                break
            nel += 1
        print("")
    else:
        print("")
    return nel
