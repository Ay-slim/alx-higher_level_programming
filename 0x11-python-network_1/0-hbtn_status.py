#!/usr/bin/python3
"""
Module for a script that fetches data with urllib
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        response_read = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(response_read)))
        print('\t- content: {}'.format(response_read))
        print('\t- utf8 content: {}'.format(response.__dict__['msg']))
