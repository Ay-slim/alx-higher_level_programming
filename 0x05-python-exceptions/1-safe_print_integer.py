#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if str(value).startswith('-'):
            isdigitcheck = str(value)[1:].isdigit()
        else:
            isdigitcheck = str(value).isdigit()
        if (isdigitcheck):
            print("{:d}".format(int(value)))
            return True
        else:
            raise SyntaxError
    except SyntaxError:
        return False
