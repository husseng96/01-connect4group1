import numpy as np
import pygame
import sys
import math
from button import *
import random


pygame.init()

#colors
WHITE = (255,255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 100, 255)
LIGHT_WHITE = (170, 170, 170)
DARK_WHITE = (100, 100, 100)
RED = (255,0,0)
YELLOW = (255,255,0)


#define our screen size
SQUARESIZE = 100


EMPTY = 0
PLAYER_PIECE = 1
COMPUTER_PIECE = 2

#Screen
width = 1280
height = 720
res = (width,height)
screen = pygame.display.set_mode(res)

BG = pygame.image.load("Dots.jpeg")
BG = pygame.transform.scale(BG, res)

#chips ratio to screen
if width > height:
    RADIUS = int(height/15)
else:
    RADIUS = int(width/15)

myfont = pygame.font.SysFont("monospace", 75)

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def board_gen_gui(screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.circle(screen, WHITE, (int((c * height/ROW_COUNT) + 1.5*RADIUS), int((r * height/ROW_COUNT) + 1.5*RADIUS)),
                                   RADIUS)

    pygame.display.update()


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, LIGHT_BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == COMPUTER_PIECE:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True


def board_gen():
    board=np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def main_menu():
    while True:
        for choice in pygame.event.get():
            if choice.type == pygame.QUIT:
                pygame.quit()

            if choice.type == pygame.MOUSEBUTTONDOWN:
                if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                        and (single_y - (button_height / 2)) <= mouse[1] <= (single_y + (button_height / 2)):
                    single()
                elif (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                             and (multi_y - (button_height/2)) <= mouse[1] <= (multi_y + (button_height/2)):
                    multi()
                elif (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                             and (rules_y - (button_height/2)) <= mouse[1] <= (rules_y + (button_height/2)):
                    rules()
                elif (button_x - (quit_width/2)) <= mouse[0] <= (button_x + (quit_width/2)) \
                             and (quit_y - (quit_height/2)) <= mouse[1] <= (quit_y + (quit_height/2)):
                    pygame.quit()

        screen.blit(BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        #Button size
        button_width = width/5
        button_height = height/15
        button_x = width/2

        #buttons
        #single player button
        single_y = height/2.7

        single_button = Button(button_x, single_y, button_width, button_height)

        if (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                and (single_y - (button_height/2)) <= mouse[1] <= (single_y + (button_height/2)):
            single_button.draw(screen, DARK_WHITE, 0, WHITE, 'One-Player')
        single_button.draw(screen, WHITE, 1, WHITE, 'One-Player')

        #two player button
        multi_y = height / 2.2

        multi_button = Button(button_x, multi_y, button_width, button_height)

        if (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                and (multi_y - (button_height/2)) <= mouse[1] <= (multi_y + (button_height/2)):
            multi_button.draw(screen, DARK_WHITE, 0, WHITE, 'Two-Player')
        multi_button.draw(screen, WHITE, 1, WHITE, 'Two-Player')

        #rules button
        rules_y = height/1.85

        rules_button = Button(button_x, rules_y, button_width, button_height)

        if (button_x - (button_width/2)) <= mouse[0] <= (button_x + (button_width/2)) \
                and (rules_y - (button_height/2)) <= mouse[1] <= (rules_y + (button_height/2)):
            rules_button.draw(screen, DARK_WHITE, 0, WHITE, 'Rules')
        rules_button.draw(screen, WHITE, 1, WHITE, 'Rules')

        #quit button
        quit_y = height/1.55
        quit_width = width/15
        quit_height = height/18

        quit_button = Button(button_x, quit_y, quit_width, quit_height)

        quit_button.draw(screen, LIGHT_WHITE, 0, BLACK, 'Quit')
        if (button_x - (quit_width/2)) <= mouse[0] <= (button_x + (quit_width/2)) \
                and (quit_y - (quit_height/2)) <= mouse[1] <= (quit_y + (quit_height/2)):
            quit_button.draw(screen, DARK_WHITE, 0, WHITE, 'Quit')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()

def single():
    while True:
        screen.fill(LIGHT_BLUE)

        board = board_gen()
        board_gen_gui(screen)

        pygame.display.update()

def multi():
    board = create_board()

    draw_board(board)
    pygame.display.update()

    game_over = False
    turn = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            screen.blit(label, (40, 10))
                            game_over = True

                # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)

def rules():
    while True:
        #filling the background
        screen.fill(LIGHT_BLUE)

        #Rules titles
        rules_title_font = pygame.font.SysFont('freesansbold',100)
        rulesText = rules_title_font.render("RULES", True, WHITE)
        title_width, title_height = rules_title_font.size('RULES')
        title_x = (width - title_width)/2

        #Listed Rules
        rules_font = pygame.font.SysFont('freesansbold', 35)
        rule1 = "- The rules of this game are simple."
        rule2 = "- Players take turns dropping chips into the 6 by 7 grid layout and their goal to winning the game is "
        rule3 = "to get four chips in a row."
        rule4 = "- Players can get four in a row in a variety of patterns: horizontally, vertically, or diagonally."
        rule5 = "- There is a possibility of a tie occurring in the game if no players get four in a row."

        text1 = rules_font.render(rule1, True, WHITE)
        text2 = rules_font.render(rule2, True, WHITE)
        text3 = rules_font.render(rule3, True, WHITE)
        text4 = rules_font.render(rule4, True, WHITE)
        text5 = rules_font.render(rule5, True, WHITE)

        #Outputting all text
        text_width, text_height = rules_font.size(rule1)
        text_y = height/3.5

        screen.blit(rulesText, (title_x, height/10))
        screen.blit(text1, (width/100, text_y))
        screen.blit(text2, (width/100, text_y + 2*text_height))
        screen.blit(text3, (width/100, text_y + 4*text_height))
        screen.blit(text4, (width/100, text_y + 6*text_height))
        screen.blit(text5, (width/100, text_y + 8*text_height))

        #Back Button
        mouse = pygame.mouse.get_pos()

        for click in pygame.event.get():
            if click.type == pygame.QUIT:
                pygame.quit()

            if click.type == pygame.MOUSEBUTTONDOWN:
                if back_x <= mouse[0] <= back_x + back_width and back_y <= mouse[1] <= back_y + back_height:
                    main_menu()

        back_width, back_height = rules_font.size("back")
        back_x = (width - back_width)/2
        back_y = 4*height / 5

        back = rules_font.render("Back", True, WHITE)
        if back_x <= mouse[0] <= back_x + back_width and back_y <= mouse[1] <= back_y + back_height:
            back = rules_font.render("Back", True, DARK_WHITE)
        screen.blit(back, (back_x, back_y))

        pygame.display.update()

main_menu()
