#!/usr/bin/python3
"""
Write a Python script that takes in a URL
and displays the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    html = requests.get(argv[1])
    if html.status_code < 400:
        print(html.text)
    else:
        print("Error code: {}".format(html.status_code))
