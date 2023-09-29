#!/usr/bin/python3
"""
Module for a script that fetches data with urllib while handling
error
"""

from urllib.error import HTTPError
import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
