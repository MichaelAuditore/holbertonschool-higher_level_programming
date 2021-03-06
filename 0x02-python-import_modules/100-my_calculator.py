#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    operators = {'+', '-', '*', '/'}
    isOperator = False
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    for i in operators:
        if sys.argv[2] == i:
            isOperator = True
            break
    if isOperator is False:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if (sys.argv[2] == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (sys.argv[2] == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (sys.argv[2] == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
