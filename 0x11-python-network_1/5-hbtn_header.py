#!/usr/bin/python3
"""
Module for a script that fetches data with the request library
and print the header
"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
