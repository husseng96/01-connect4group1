import pygame
import sys

pygame.init()

res = (720, 720)

screen = pygame.display.set_mode(res)

white = (255, 255, 255)

white_light = (170, 170, 170)

white_dark = (100, 100, 100)

width = screen.get_width()

height = screen.get_height()

gamefont = pygame.font.SysFont('Corbel', 35)

singeoption = gamefont.render("Single Player", True, white)

multioption = gamefont.render("Multiplayer", True, white)

rulesoption = gamefont.render("Rules", True, white)

quitoption = gamefont.render('Quit', True, white)

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
