#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    llaves = list(a_dictionary.keys())
    llaves.sort()
    for key in llaves:
        print("{0}: {1}".format(key, a_dictionary[key]))
