def print_last_digit(number):
    number = (number * -1) % 10 if number < 0 else number % 10
    print("{:d}".format(number), end="")
    return (number)