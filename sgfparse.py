#!/usr/bin/python3

"""
regex to search sgfs by metadata
"""

import re

from sys import argv,exit, stdout, stderr

def process(filename):

    # open file
    with open(filename) as f:
        raw = f.read()

    # make dictionary
    KEYS = {}

    # Look for keys
    L_ = re.findall('[A-Z]{1,2}\[[^\]]+\]', raw)
    L = [item for item in L_ if not item.startswith('B[') \
            and not item.startswith('W[') and not item.startswith('BL[')
            and not item.startswith('WL[') and not item.startswith('C[')]

    for item in L:
        i = item.index('[') 
        j = item.index(']') 
        KEYS[item[:i]] = item[i+1:j]
    return KEYS


if __name__ == '__main__':
    if not argv[1:]:
        print("Need sgf filename")
        exit(1)

    if not argv[2:]:
        print("Need key")
        exit(2)

    keys = process(argv[1])
    try:
        print(keys[argv[2]])
    except KeyError:
        stderr.write("Key not found: " + argv[2] + '\n')
