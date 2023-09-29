#!/usr/bin/python3
"""
Module for a script that posts data with the request library
and sends a parameter
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        j = r.json()
        print(j, 'JJJJ')
        if len(j.keys()):
            for key, val in j.items():
                print('[{}] {}'.format(key, val))
        else:
            print('No result')
    except ValueError as e:
        print('Not a valid JSON')
