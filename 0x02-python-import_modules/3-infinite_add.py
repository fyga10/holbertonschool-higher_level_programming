#!/usr/bin/python3
from sys import argv
length = len(argv)
add = 0
for i in range(1, length):
    add += int(argv[i])
print(add)
