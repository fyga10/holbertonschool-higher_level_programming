#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as url_r:
            response = url_r.read()
            print(str(response, 'utf-8'))
    except urllib.error.HTTPError:
        print("Error code: {}".format(sys.exc_info()[1].code))
