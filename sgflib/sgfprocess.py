#!/usr/bin/python3

import re
import os
from sgflib import boards, Pattern

from sys import argv,exit, stdout, stderr

# Build a list of moves
# sgf files have moves in the form [qd]
#   The first coordinate is the column
#   The second coordinate is the row

def pull_moves_raw(raw):
    moves = []
    lines = raw.split('\n')
    for line in lines:
        if line.startswith(';'):
            # Player
            assert line[1] == "B" or line[1] == "W"

            # Regular expression to find two characters following '['
            m = re.search('(?<=\[)[a-s]{2}', line)
            if m:
                pair = m.group(0)
                col = translate(pair[0])
                row = translate(pair[1])
                move = (col,row)
                moves.append(move)
    return moves
 

def pull_moves(filename=None, raw=None):
    if raw:
        return pull_moves_raw(raw)
    elif filename:
        with open(filename) as f:
            raw = f.read()
            return pull_moves_raw(raw)
    else:
        print("pull_moves must have either a filename or raw data")
        exit(1)

def translate(let):
    alphabet = 'abcdefghijklmnopqrs'
    assert let in alphabet
    return alphabet.index(let)

def make_keys(raw):
    KEYS = {}
    L_ = re.findall('[A-Z]{1,2}\[[^\]]+\]', raw)
    L = [item for item in L_ if not item.startswith('B[') \
            and not item.startswith('W[') and not item.startswith('BL[')
            and not item.startswith('WL[') and not item.startswith('C[')]
    #print(L)
    for item in L:
        i = item.index('[') 
        j = item.index(']') 
        KEYS[item[:i]] = item[i+1:j]
    return KEYS
    #print(KEYS)

def display(board):
    for row in board:
        for cell in row:
            print(str(cell) + ' ', end='')
        print()
    wait = input()

def check_opening(filename, me, opening):
    game, win,color = process_sgf(filename, me)
    print(replay(game, check_opening=opening, color=color), win)

def replay(game, check_opening=False, color=None, reverse=False):
    B = '\u25cb'
    W = '\u25cf'
    if reverse:
        tmp = B
        B = W
        W = tmp
    PLAYER = [W,B]
    tmp_dict = {'B':B, 'W':W}

    board = boards.make_board()
    cur = 0
    if check_opening:
        try:
            pattern, move_num = Pattern.registry[check_opening]
        except KeyError:
            return "Pattern " + check_opening + " not found in registry"
    for col,row in game:
        cur += 1
        board[row][col] = PLAYER[cur % 2]
        if not check_opening:
            out = os.system('clear')
        #print("Move:", cur)
        
        # At move move_num, compare to kobayashi
        if check_opening and cur == move_num:
            # If the wrong player is playing the pattern
            if tmp_dict[color] != board[row][col]:
                return False

            return boards.check_all(board, pattern)
        
        if not check_opening:
            display(board)

def process_sgf(filename, me):
    # open file
    with open(filename) as f:
        raw = f.read()

    # KEYS
    KEYS = make_keys(raw)

    # Color
    color = "B"
    if KEYS['PW'].lower() == me:
        color = "W"

    # WIN
    win = False
    try:
        if KEYS['RE'][0] == color:
            win = True
    except KeyError:
        stderr.write("No result on this game: " + filename + "\n")
        exit(3)
    
    # Moves
    moves = pull_moves(raw=raw)

    return moves, win, color

if __name__ == '__main__':
    if not argv[1:]:
        print("Need sgf filename")
        exit(1)

    if not argv[1].endswith('.sgf'):
        print("Need sgf extension")
        exit(2)

    if not argv[2:]:
        print("Need account name")
        exit(3)

    moves,win,color = process_sgf(argv[1], argv[2].lower())
    replay(moves)

