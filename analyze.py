#!/usr/bin/python3

from sys import argv, exit, stderr

if __name__ == '__main__':
    if not argv[1:]:
        print("Need filename")
        exit(1)

    filename = argv[1]
    base = filename.split('.')[0]
    user,year,pattern = base.split('-')

    won = 0
    total = 0
    try:
        with open(filename) as f:
            for line in f:
                result = line.split(':')[1].strip()
                if result == "True":
                    won += 1
                total += 1
        print(user, "won", won, "games out of", total, "in", year, "using", pattern)
    except FileNotFoundError:
        stderr.write("File not found\n")



