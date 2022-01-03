#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        first = sentence[0]
    else:
        first = None
    return len(sentence), first
