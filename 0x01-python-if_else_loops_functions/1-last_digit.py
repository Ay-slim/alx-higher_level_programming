#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print_val = "Last digit of {} is {} and is "
last_digit = 0
sign = number / abs(number)
if number > 9 or number < -9:
    last_digit = ((number * sign) % 10) * sign
else:
    last_digit = number
if last_digit > 5:
    print_val += "greater than 5"
elif last_digit == 0:
    print_val += "0"
else:
    print_val += "less than 6 and not 0"
print(print_val.format(number, int(last_digit)))
