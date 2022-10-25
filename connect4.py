
import numpy as np
import pygame
import sys

pygame.init()

#color blue
BLUE=(0,0,200)
BLACK = (0,0,0)
PIXELS_FOR_SQUARES=100
RADIUS = int(PIXELS_FOR_SQUARES/2 - 5)

#chips red - 1st, yellow - 2nd


game_over=True
def main():
    #create board
    board=board_gen()

    #print(board)
    #pygame GUI
    pygame.init()
    gui_size=(900,900)
    #gui=pygame.display.set_mode(gui_size)
    screen=pygame.display.set_mode(gui_size)
    pygame.display.set_caption('Connect 4')

res = (720, 720)

screen = pygame.display.set_mode(res)

white = (255, 255, 255)

white_light = (170, 170, 170)

white_dark = (100, 100, 100)

width = screen.get_width()

height = screen.get_height()

gamefont = pygame.font.SysFont('Ariel', 35)

singeoption = gamefont.render("Single Player", True, white)

multioption = gamefont.render("Multiplayer", True, white)

rulesoption = gamefont.render("Rules", True, white)

quitoption = gamefont.render('Quit', True, white)

def board_gen_gui(screen):
    for c in range(7):
        for r in range(6):
            pygame.draw.rect(screen, BLUE, (c*PIXELS_FOR_SQUARES, r*PIXELS_FOR_SQUARES, PIXELS_FOR_SQUARES,
                                            PIXELS_FOR_SQUARES))
            pygame.draw.circle(screen, BLACK, (int(c*PIXELS_FOR_SQUARES + PIXELS_FOR_SQUARES/2),
                               int(r*PIXELS_FOR_SQUARES + PIXELS_FOR_SQUARES + PIXELS_FOR_SQUARES/2)),
                               RADIUS)

    pygame.display.update()

def board_gen():
    board=np.zeros((6,7))
    return board

while True:
    for choice in pygame.event.get():
        if choice.type == pygame.QUIT:
            pygame.quit()

        if choice.type == pygame.MOUSEBUTTONDOWN:
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] < + height / 2 + 40:
                pygame.quit()

    screen.fill((60, 25, 60))

    mouse = pygame.mouse.get_pos()

    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, white_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, white_dark, [width / 2, height / 2, 140, 40])

    screen.blit(quitoption, (width / 2 + 50, height / 2))

    screen.blit(singeoption,(width / 2 , height / 2 - 100))



    pygame.display.update()
    board_gen_gui(screen)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()





main()
