#!/usr/bin/python3

from sgflib import sgfprocess
from sys import argv, exit

def get_input(msg, allow, default=None):
    result = None
    while not result:
        attempt = input(msg).lower()
        if len(attempt) == 0:
            return default
        if attempt in allow:
            result = attempt
    return result

def usage():
    print("[*] This program has two accepted use cases:")
    print("Usage 1: {} [sgf]".format(argv[0]))
    print("     This will simply replay the game on the terminal")
    print("     Press <Enter> to proceed through moves")
    print("Usage 2: {} [sgf] [account] [opening]".format(argv[0]))
    print("     This will check [sgf] to see if [account] won the game using [opening].")
    print("     It will return two booleans:")
    print("       - the first is whether or not [opening] was used.")
    print("       - the second is whether or not [account] won.")

if __name__ == '__main__':
    if not argv[1:]:
        usage()
        exit(1)

    if not argv[2:]:
        reverse = get_input("Are you on a black screen? [Yes/no] ", ['y', 'ye', 'yes', 'n', 'no'], default='y')
        if reverse.startswith('y'):
            reverse = 0
        else:
            reverse = 1
        moves = sgfprocess.pull_moves(filename=argv[1])
        sgfprocess.replay(moves, reverse=reverse)
        exit(0)

    if not argv[3:]:
        usage()
        exit(3)

    sgfprocess.check_opening(argv[1], argv[2], argv[3])
