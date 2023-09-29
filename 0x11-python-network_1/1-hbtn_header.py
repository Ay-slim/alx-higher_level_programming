#!/usr/bin/python3
"""
Module for a script that fetches response header with urllib
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
