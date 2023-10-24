#!/usr/bin/python3
"""
Module for a script that posts data with the request library
and prints error if any
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if int(r.status_code) >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
