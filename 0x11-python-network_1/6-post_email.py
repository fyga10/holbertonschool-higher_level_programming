#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the value of the variable
"""
from requests import post
from sys import argv
if __name__ == "__main__":
    dict = {'email': argv[2]}
    html = post(argv[1], data=dict)
    print(html.text)
