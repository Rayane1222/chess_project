"""
here we will be the main file of the program
"""

#pip install pygame

import pygame as p
import ChessEngine as ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8  # board is a 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  #fps pour les animention avec pygame
IMAGES = {}

'''
here i want that the images dont lag for me like i need the images stay in the ram in the memory et pas every move i have to reload
the images 

'''


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
here i will handle user input b7Al moves and updating graphics
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible of the graphics in the current game state 
'''
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

#here I will draw the squards u know for the boad
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))



# here i will draw the pieces from dak fichier ./images
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #not empty
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))














if __name__ == '__main__':
    main()
