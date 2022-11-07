import numpy as np
import sys
import math
from Button import *
import random

pygame.init()

#colors
WHITE = (255,255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255,0,0)
YELLOW = (255,255,0)
LIGHT_BLUE = (0, 100, 255)
LIGHT_WHITE = (170, 170, 170)
DARK_WHITE = (100, 100, 100)
RED = (255, 0, 0)
YELLOW = (255,255,0)

#define our screen size
#SQUARESIZE = 100

EMPTY = 0
FIRST_PIECE = 1
SECOND_PIECE = 2

#Screen
width = 1280
height = 720
res = (width,height)
screen = pygame.display.set_mode(res)

BG = pygame.image.load("Dots.jpeg")
BG = pygame.transform.scale(BG, res)

FIRST_PIECE = 1
SECOND_PIECE = 2

#chips ratio to screen
if width > height:
    RADIUS = int(height/18)
else:
    RADIUS = int(width/18)

rows = 6
cols = 7

def create_board():
    board = np.zeros((rows,cols))
    return board

def board_gen_gui(screen, color, board):
    screen.fill(color)

    cir_x = 1.5 * RADIUS
    cir_y = height - 1.5*RADIUS
    for c in range(cols):
        for r in range(rows):
            pygame.draw.circle(screen, WHITE, (cir_x, cir_y), RADIUS)
            cir_y = cir_y - 2.5 * RADIUS
        cir_y = height - 1.5*RADIUS
        cir_x = cir_x + 2.5 * RADIUS

    play_x = 1.5 * RADIUS
    play_y = height - 1.5 * RADIUS
    for c in range(cols):
        for r in range(rows):
            if board[r][c] == FIRST_PIECE:
                pygame.draw.circle(screen, RED, (play_x, play_y), RADIUS)
            elif board[r][c] == SECOND_PIECE:
                pygame.draw.circle(screen, YELLOW, (play_x, play_y), RADIUS)
            play_y = play_y - 2.5 * RADIUS
        play_y = height - 1.5 * RADIUS
        play_x = play_x + 2.5 * RADIUS

    pygame.display.update()


#def draw_board(board):
#    for c in range(COLUMN_COUNT):
#        for r in range(ROW_COUNT):
#            pygame.draw.rect(screen, LIGHT_BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
#            pygame.draw.circle(screen, BLACK, (
#            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

#    for c in range(COLUMN_COUNT):
#        for r in range(ROW_COUNT):
#            if board[r][c] == PLAYER_PIECE:
#                pygame.draw.circle(screen, RED, (
#                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
#            elif board[r][c] == COMPUTER_PIECE:
#                pygame.draw.circle(screen, YELLOW, (
#                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
#    pygame.display.update()

def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[rows - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(rows):
        if board[r][col] == 0:
            return r


#def print_board(board):
#    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(cols - 3):
        for r in range(rows):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(cols):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(cols - 3):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(cols - 3):
        for r in range(3, rows):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True

def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[rows - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(rows):
        if board[r][col] == 0:
            return r


#def print_board(board):
#    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(cols - 3):
        for r in range(rows):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(cols):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(cols - 3):
        for r in range(rows - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][
                c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(cols - 3):
        for r in range(3, rows):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][
                c + 3] == piece:
                return True

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

def minmax(board, depth, alpha, beta, maxplayer):
    moveoptions = get_value_locations(board)
    if maxplayer:
        value = -math.inf
        column = random.choice(moveoptions)
        for col in moveoptions:
            row = get_next_open_row(board, col)
            copyofboard = board.copy()
            #drop_piece(copyofboard, row, col, piece, )

def get_value_locations(board):
    valid_locations = []
    for col in range(7):
        if is_valid_location(board,col):
            valid_locations.append(col)
        return valid_locations

def computermove(board):
    #posx = event.pos[0]
    #col = int(math.floor(posx / len_piece))
    pygame.time.wait(800)
    compcol = random.randint(0,6)
    if is_valid_location(board, compcol):
        row = get_next_open_row(board, compcol)
        drop_piece(board, row, compcol, 2)

        if winning_move(board, 2):
            label = myfont.render("Player 2 wins!!", 1, YELLOW)
            screen.blit(label, (40, 10))
            game_over = True
            return game_over


def single():
    while True:
        screen.fill(LIGHT_BLUE)

        board = board_gen()
        board_gen_gui(screen, LIGHT_BLUE,board)

        strip_w = width - (14 * RADIUS)
        strip_h = height - (15 * RADIUS)
        strip = pygame.Rect(0, 0, strip_w, strip_h)

        len_piece = strip_w / cols

        game_over = False
        turn = 0

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, LIGHT_BLUE, strip)
                    posx = event.pos[0]
                    if posx < strip_w - RADIUS:
                        if turn == 0:
                            pygame.draw.circle(screen, RED, (posx, int(height / 10)), RADIUS)
                        #else:
                            #pygame.draw.circle(screen, YELLOW, (posx, int(height / 10)), RADIUS)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(event.pos)
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / len_piece))
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 1)

                            if winning_move(board, 1):
                                label = myfont.render("Player 1 wins!!", 1, RED)
                                screen.blit(label, (40, 10))
                                game_over = True

                    # Ask for Player 2 Input
                    # Computer is yellow

                        '''
                        col = int(math.floor(posx / len_piece))
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 2)

                            if winning_move(board, 2):
                                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                                screen.blit(label, (40, 10))
                                game_over = True
                                '''

                    board_gen_gui(screen, LIGHT_BLUE, board)

                    turn += 1
                    turn = turn % 2

                if turn == 1:
                    posx = event.pos[0]
                    gameresult = computermove(board)
                    board_gen_gui(screen, LIGHT_BLUE, board)

                    turn += 1
                    turn = turn % 2

                    if gameresult:
                        pygame.time.wait(1000)

                pygame.display.update()

def multi():
    while True:
        board = create_board()
        board_gen_gui(screen, BLUE, board)

        strip_w = width - (14*RADIUS)
        strip_h = height - (15*RADIUS)
        strip = pygame.Rect(0, 0, strip_w, strip_h)

        len_piece = strip_w / cols

        game_over = False
        turn = 0

        heading_font = pygame.font.SysFont("monospace", 50)

        while not game_over:
            if turn == 0:
                whose_turn = heading_font.render("Player 1's Turn", True, RED)
                head_width, head_height = heading_font.size("Player 1's Turn")
            else:
                whose_turn = heading_font.render("Player 2's Turn", True, YELLOW)
                head_width, head_height = heading_font.size("Player 2's Turn")

            heading_y = (strip_h - head_height) / 2
            screen.blit(whose_turn, (strip_w, heading_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLUE, strip)
                    posx = event.pos[0]
                    if posx < strip_w-RADIUS:
                        if turn == 0:
                            pygame.draw.circle(screen, RED, (posx, int(height/10)), RADIUS)
                        else:
                            pygame.draw.circle(screen, YELLOW, (posx, int(height/ 10)), RADIUS)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / len_piece))
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 1)

                            if winning_move(board, 1):
                                label = heading_font.render("Player 1 wins!!", 1, RED)
                                screen.blit(label, (40, 10))
                                game_over = True

                    # Ask for Player 2 Input
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / len_piece))
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 2)

                            if winning_move(board, 2):
                                label = heading_font.render("Player 2 wins!!", 1, YELLOW)
                                screen.blit(label, (40, 10))
                                game_over = True

                    board_gen_gui(screen, BLUE, board)

                    turn += 1
                    turn = turn % 2

                    if game_over:
                        pygame.time.wait(500)

                pygame.display.update()

def rules():
    while True:
        #filling the background
        #screen.fill(LIGHT_BLUE)

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
