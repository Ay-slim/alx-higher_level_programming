#!/usr/bin/python3
"""
Module for a script that fetches github user id
"""

import requests
import sys

if __name__ == "__main__":
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer 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",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'.format(
            sys.argv[2], sys.argv[1])
    r = requests.get(url, headers=headers)
    for i in r.json():
        print('{}: {}'.format(i['sha'], i['commit']['author']['name']))
