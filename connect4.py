import numpy as np
import pygame
import sys

pygame.init()

#colors
LIGHT_BLUE=(0,102,255)
LIGHT_WHITE = (170, 170, 170)
DARK_WHITE = (100, 100, 100)

#Screen
width = 1280
height = 720
res = (width,height)
screen = pygame.display.set_mode(res)

rows = 6
cols = 7

BG = pygame.image.load("Dots_BG.jpeg")
BG = pygame.transform.scale(BG, res)

#Text
game_font = pygame.font.SysFont('arial', 35)

#Button
button_width = 210
button_height = 40

single_option = game_font.render("Single Player", True, "white")
multi_option = game_font.render("Two player", True, "white")
rules_option = game_font.render("Rules", True, "white")
quit_option = game_font.render('Quit', True, "black")

if width > height:
    RADIUS = int(height/15)
else:
    RADIUS = int(width/15)


def single():
    while True:
        screen.fill(LIGHT_BLUE)

        board=board_gen()
        board_gen_gui(screen)

        pygame.display.update()

def multi():
    while True:
        screen.fill("blue")

        board=board_gen()
        board_gen_gui(screen)

        pygame.display.update()

def rules():
    while True:
        screen.fill("white")

        pygame.display.update()

def board_gen_gui(screen):
    for c in range(cols):
        for r in range(rows):
            pygame.draw.circle(screen, "white", (int((c * height/rows) + 1.5*RADIUS), int((r * height/rows) + 1.5*RADIUS)),
                                   RADIUS)

    pygame.display.update()

def board_gen():
    board=np.zeros((rows,cols))
    return board

def main_menu():
    while True:
        for choice in pygame.event.get():
            if choice.type == pygame.QUIT:
                pygame.quit()

            if choice.type == pygame.MOUSEBUTTONDOWN:
                if button_x <= mouse[0] <= button_x + button_width and single_y <= mouse[1] <= single_y + button_height:
                    single()
                elif button_x <= mouse[0] <= button_x + button_width and multi_y <= mouse[1] <= multi_y + button_height:
                    multi()
                elif button_x <= mouse[0] <= button_x + button_width and rules_y <= mouse[1] <= rules_y + button_height:
                    rules()
                elif quit_x-10 <= mouse[0] <= quit_x+76 and quit_y <= mouse[1] <= quit_y + 40:
                    pygame.quit()

        screen.blit(BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        #Button size
        button_width = width/5
        button_height = height/15
        button_x = width/2.5

        #Single button
        single_y = height/2.7
        pygame.draw.rect(screen, "white", [button_x, single_y, button_width, button_height], 1, 10)
        if button_x <= mouse[0] <= button_x + button_width and single_y <= mouse[1] <= single_y + button_height:
            pygame.draw.rect(screen, DARK_WHITE, [button_x, single_y, button_width, button_height], 0, 10)
        screen.blit(single_option,(button_x+25, single_y))

        #Multi button
        multi_y = height/2.2
        pygame.draw.rect(screen, "white", [button_x, multi_y, button_width, button_height], 1, 10)
        if button_x <= mouse[0] <= button_x + button_width and multi_y <= mouse[1] <= multi_y + button_height:
            pygame.draw.rect(screen, DARK_WHITE, [button_x, multi_y, button_width, button_height], 0, 10)
        screen.blit(multi_option,(button_x+45, multi_y))

        #Rules Button
        rules_y = height/1.85
        pygame.draw.rect(screen, "white", [button_x, rules_y, button_width, button_height], 1, 10)
        if button_x <= mouse[0] <= button_x + button_width and rules_y <= mouse[1] <= rules_y + button_height:
            pygame.draw.rect(screen, DARK_WHITE, [button_x, rules_y, button_width, button_height], 0, 10)
        screen.blit(rules_option, (button_x+80, rules_y))

        #Quit Button
        quit_x = width/2.15
        quit_y = height/1.55
        pygame.draw.rect(screen, LIGHT_WHITE, [quit_x, quit_y, 86, 40])
        if quit_x <= mouse[0] <= quit_x+86 and quit_y <= mouse[1] <= quit_y + 40:
            pygame.draw.rect(screen, DARK_WHITE, [quit_x, quit_y, 86, 40])
        screen.blit(quit_option, (quit_x+10, quit_y))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

main_menu()
