#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in order to solve this challenge.
"""
import requests
from sys import argv

if __name__ == '__main__':
    urls = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    htm = requests.get(urls)
    commi = htm.json()
    for commit in commi[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
