#!/usr/bin/python3
"""
Module for a script that fetches github user id
"""

import requests
import sys

if __name__ == "__main__":
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(sys.argv[2]),
        "X-GitHub-Api-Version": "2022-11-28"
    }
    r = requests.get('https://api.github.com/user', headers=headers)
    if r.status_code == 200:
        print(r.json()['id'])
    else:
        print('None')
