#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number != 0:
        sign = number / abs(number)
    if number > 9 or number < -9:
        last_digit = int((number * sign) % 10)
    else:
        last_digit = number
    print("{}".format(last_digit), end="")
    return last_digit
