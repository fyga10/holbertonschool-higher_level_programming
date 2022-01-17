#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = ""
    try:
        res = fct(*args)
    except Exception as E:
        sys.stderr.write("Exception: {}\n".format(E))
        return None
    return res
