"""
here we will be the main file of the program
"""

#pip install pygame

import pygame as p
import ChessEngine as ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 # board is a 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #fps pour les animention avec pygame
IMAGES = {}

'''
here i want that the images dont lag for me like i need the images stay in the ram in the memory et pas every move i have to reload
the images 

'''

def loadImages():

