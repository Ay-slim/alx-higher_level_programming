#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def basic_calc():
    calc_dict = {"+": add, "-": sub, "*": mul, "/": div}
    args = sys.argv
    operator_failure = "Unknown operator. Available operators: +, -, * and /"
    arg_count_failure = "Usage: ./100-my_calculator.py <a> <operator> <b>"
    if len(args) != 4:
        print("{}".format(arg_count_failure))
        sys.exit(1)
    if args[2] not in list(calc_dict.keys()):
        print("{}".format(operator_failure))
        sys.exit(1)
    first = int(args[1])
    second = int(args[3])
    print("{} {} {} = {}".format
          (args[1], args[2], args[3], calc_dict[args[2]](first, second)))
    sys.exit(0)


if __name__ == "__main__":
    basic_calc()
