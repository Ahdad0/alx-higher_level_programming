#!/usr/bin/python3
"""
given username and pw as param, get your id from Github api
usage: ./10-my_github.py [github_username] [github_pw]
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
