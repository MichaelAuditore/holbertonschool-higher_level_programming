#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    arg = "argument:" if (len(sys.argv) == 2) else "arguments."\
          if (len(sys.argv) == 1) else "arguments:"
    length = 0 if len(sys.argv) == 1 else len(sys.argv) - 1
    print("{} {}".format(length, arg))
    nEl = 1
    for i in sys.argv:
        if (i != sys.argv[0]):
            print("{}: {}".format(nEl, i))
            nEl += 1
