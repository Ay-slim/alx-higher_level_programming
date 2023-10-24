#!/usr/bin/python3
"""
Module for a script that posts data with the request library
and prints the response
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(r.text)
