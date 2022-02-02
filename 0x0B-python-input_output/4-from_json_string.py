#!/usr/bin/python3
"""from_json_string function"""


import json


def from_json_string(my_str):
    """Receives object and returns its JSON representation"""

    obj = json.loads(my_str)
    return obj
