#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    datas = parse.urlencode({"email": sys.argv[2]}).encode()
    requ = request.Request(sys.argv[1], data=datas)
    with request.urlopen(requ) as response:
        print(str(response.read(), "utf-8"))
