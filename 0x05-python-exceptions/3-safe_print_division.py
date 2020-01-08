#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    flag = True
    try:
        result = a / b
    except ZeroDivisionError:
        flag = False
    except ValueError:
        flag = False
    finally:
        if flag:
            print("Inside result: {}".format(result))
            return result
        else:
            print("Inside result: None")
            return None
