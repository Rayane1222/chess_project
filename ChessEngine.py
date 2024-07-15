"""
here alferda we will store the information about the current game and the possible moves and stor the moves logs
"""


class GameState():

    #here a did create a sahbi board dyal 8x8 2D list and each of element of the list has 2 charactere
    #the fist charactere f l3iba represent a color of a piece like b black w white
    #the second is the type i just learn from internet king K queen Q rook R pawns p bishops B knights K
    # -- is like nothing khawi empty space o sf
    def __init__(self):
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

        self.whiteToMove = True
        self.moveLog = []










