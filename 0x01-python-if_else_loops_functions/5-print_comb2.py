#!/usr/bin/python3
for cons in range(00, 100):
    if cons < 99:
        print("{:02d}".format(cons), end=", ")
    else:
        print("{:d}".format(cons))
