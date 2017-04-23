from sgflib import boards
from sgflib.Reg import registry, register, Pattern

B = '\u25cb'
W = '\u25cf'

"""
This file holds static board patterns
Each class uses Pattern as a metaclass,
    so that they will be auto-added to a registry

To build your own, follow this simple template

# First name it
class MyPattern(metaclass=Pattern):
    # Make a blank board
    MYPAT = boards.make_board()

    # Add the moves to be part of the pattern
    # Example: two black stones and two white stones
    #   on 4-4 points
    MYPAT[3][3] = W
    MYPAT[15][3] = W
    MYPAT[3][15] = B
    MYPAT[15][15] = B
    # Note that B and W are constants
    # (unicode characters for filled/unfilled circles)

    # Specify the move number for the pattern to be checked at
    # Example: Check the pattern after move 4
    move_num = 4

    # This tuple is what gets added to the registry
    pattern = MYPAT, move_num

# That's it!  Have fun!
"""

class Nirensei(metaclass=Pattern):
    NIRE = boards.make_board()
    NIRE[3][15] = B
    NIRE[15][15] = B
    move_num = 3
    pattern = NIRE, move_num

class ThreeFour(metaclass=Pattern):
    THFO = boards.make_board()
    THFO[3][16] = B
    THFO[16][15] = B
    move_num = 3
    pattern = THFO, move_num

class MiniChinese(metaclass=Pattern):
    MINI = boards.make_board()

    # BLACK
    MINI[3][16] = B
    #MINI[16][15] = B
    MINI[2][5] = B
    MINI[2][10] = B

    # WHITE
    MINI[3][3] = W
    #MINI[3][15] = W
    #MINI[5][2] = W

    move_num = 7

    pattern = MINI, move_num

class Chinese(metaclass=Pattern):
    CHIN = boards.make_board()
    
    # BLACK
    CHIN[3][15] = B
    CHIN[16][15] = B
    CHIN[10][16] = B

    # WHITE
    CHIN[3][3] = W
    CHIN[15][3] = W

    # Move number
    move_num = 5

    pattern = CHIN, move_num


class Kobayashi(metaclass=Pattern):
    KOBA = boards.make_board()

    # BLACK
    KOBA[3][15] = B
    KOBA[16][15] = B
    KOBA[16][5] = B
    KOBA[15][9] = B

    # WHITE
    # KOBA[3][3] = W
    KOBA[15][3] = W
    # KOBA[13][2] = W

    # Move number
    move_num = 7

    pattern = KOBA, move_num
