import numpy as np
import pygame
import sys

#color blue
BLUE=(0,0,200)
PIXELS_FOR_SQUARES=100

game_over=True
def main():
    #create board
    board=board_gen()
    #print(board)
    #pygame GUI
    pygame.init()
    gui_size=(900,900)
    gui=pygame.display.set_mode(gui_size)
    screen=pygame.display.set_mode(gui_size)
    pygame.display.set_caption('Connect 4')
    board_gen_gui(board)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        

def board_gen():
    board=np.zeros((6,7))
    return board

def board_gen_gui(board):
    for c in range(7):
        for r in range(6):
            pygame.draw.rect(screen, BLUE, (c*PIXELS_FOR_SQUARES, r*PIXEL_FOR_SQUARES, PIXEL_FOR_SQUARES_PIXEL_FOR_SQUARES))
    
main()
