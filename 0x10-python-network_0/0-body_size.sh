#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
expr $(echo $(curl "$1" 2> /dev/null) | wc -c) - 1
