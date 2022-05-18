#!/bin/bash
# Post with body parameters
curl -s -o /dev/null -w "%{http_code}" "$1"
