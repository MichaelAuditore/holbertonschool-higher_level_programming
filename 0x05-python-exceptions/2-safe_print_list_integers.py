#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nel = 0
    if not my_list:
        print()
        return nel
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nel += 1
        except ValueError:
            continue
        except TypeError:
            continue
    print()
    return nel
