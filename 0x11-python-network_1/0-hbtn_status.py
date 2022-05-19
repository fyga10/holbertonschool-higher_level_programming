#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

from urllib import parse, request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as url_r:
        response = url_r.read()
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(str(response, 'utf-8')))
