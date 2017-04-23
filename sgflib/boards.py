#!/usr/bin/python3

B = '\u25cb'
W = '\u25cf'

def display(board):
    for row in board:
        for cell in row:
            print(str(cell) + ' ', end='')
        print()
    wait = input()

def make_board():
    UL = '\u250c'
    UR = '\u2510'
    LL = '\u2514'
    LR = '\u2518'
    VERT = '\u2502'
    HORZ = '\u2500'
    SQ = '+'
    #SQ = '\u271b'
    #SQ = '\u253c'

    board = []
    TOPROW = [UL] + [HORZ]*17 + [UR]
    MIDROW = [VERT] + [SQ]*17 + [VERT]
    BOTROW = [LL] + [HORZ]*17 + [LR]
    
    board.append(TOPROW.copy())
    for i in range(17):
        board.append(MIDROW.copy())
    board.append(BOTROW.copy())
    return board

def pattern_in_board(board,pattern):
    for i,row in enumerate(pattern):
        for j,cell in enumerate(row):
            if pattern[i][j] in [B,W] and pattern[i][j] != board[i][j]:
                return False
    return True


def check_all(board,pattern):
    # Check identity
    #if board == pattern:
    if pattern_in_board(board,pattern):
        return True

    # Check rotation by 90
    board90 = rot_90(board)
    #if board90 == pattern:
    if pattern_in_board(board90, pattern):
        return True

    # Check rotation by 180
    board180 = rot_90(board90)
    #if board180 == pattern:
    if pattern_in_board(board180, pattern):
        return True

    # Check rotation by 270
    board270 = rot_90(board180)
    #if board270 == pattern:
    if pattern_in_board(board270,pattern):
        return True

    # Check horizontal flip
    fboard = flip(board)
    #if fboard == pattern:
    if pattern_in_board(fboard, pattern):
        return True

    # Check horizontal flip + rotation by 90
    fboard90 = rot_90(fboard)
    #if fboard90 == pattern:
    if pattern_in_board(fboard90, pattern):
        return True

    # Check horizontal flip + rotation by 180
    fboard180 = rot_90(fboard90)
    #if fboard180 == pattern:
    if pattern_in_board(fboard180, pattern):
        return True

    # Check horizontal flip + rotation by 270
    fboard270 = rot_90(fboard180)
    #if fboard270 == pattern:
    if pattern_in_board(fboard270, pattern):
        return True

    return False

def help_rot(c):
    UL = '\u250c'
    UR = '\u2510'
    LL = '\u2514'
    LR = '\u2518'
    VERT = '\u2502'
    HORZ = '\u2500'
    special = [UL, UR, LL, LR, VERT, HORZ]
 
    D = {UL:LL, UR:UL, LR:UR, LL:LR, VERT:HORZ, HORZ:VERT}
    if c in special:
        return D[c]
    else:
        return c


def rot_90(board):
    newboard = []
    for i in range(19):
        row = [help_rot(R[i]) for R in board]
        newboard = [row] + newboard
    return newboard

def flip(board):
    UL = '\u250c'
    UR = '\u2510'
    LL = '\u2514'
    LR = '\u2518'
 
    newboard = []
    for row in board:
        newboard.append(row.copy())
        newboard[-1].reverse()
    newboard[0][0] = UL
    newboard[0][-1] = UR
    newboard[-1][0] = LL
    newboard[-1][-1] = LR
    return newboard

def test():
    TEST = make_board()
    TEST[3][16] = B
    TEST[2][14] = B

    PATT = make_board()
    PATT[16][3] = B
    PATT[14][2] = B

    #display(TEST)
    #display(PATT)

    #check_all(TEST, PATT)

    # 4-4 and 3-4
    # KOBAYASHI
    # CHINESE

    KOBA = make_koba()

    display(KOBA)

    
    
    # Two 3-4
    # Mini chinese
    # Micro chinese


    #display(TEST)
    #display(flip(TEST))
    #display(TEST)
    #for i in range(3):
    #    TEST = rot_90(TEST)
    #    display(TEST)

if __name__ == '__main__':
    test()

