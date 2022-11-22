import numpy as np
import sys
import math
import random
from Button import *
from pygame import mixer
from colour import Color


############################################### new code snippet to validate colours ###############
def validateColors(colortxt):
    try:
        Color(colortxt.replace(" ", ""))
        return True
    except:
        return False


##############################################3  end of code


def create_board():
    """ It creates a board of zeros with the dimensions of rows and cols

    :return: A 2D array of zeros.
    """
    board = np.zeros((rows, cols))
    return board


def board_gen_gui(screen, color, board, player_colors):  ############ added new parameter here
    """ It draws the board and the pieces on the board

    :param screen: the screen object that we created in the previous step
    :param color: the background color of the board
    :param board: the board that we're going to be drawing
    """
    screen.fill(color)

    cir_x = 1.5 * RADIUS
    cir_y = height - 1.5 * RADIUS
    for c in range(cols):
        for r in range(rows):
            pygame.draw.circle(screen, WHITE, (cir_x, cir_y), RADIUS)
            cir_y = cir_y - 2.5 * RADIUS
        cir_y = height - 1.5 * RADIUS
        cir_x = cir_x + 2.5 * RADIUS

    play_x = 1.5 * RADIUS
    play_y = height - 1.5 * RADIUS
    for c in range(cols):
        for r in range(rows):
            if board[r][c] == FIRST_PIECE:
                pygame.draw.circle(screen, player_colors[0], (play_x, play_y), RADIUS)
            elif board[r][c] == SECOND_PIECE:
                pygame.draw.circle(screen, player_colors[1], (play_x, play_y), RADIUS)
            play_y = play_y - 2.5 * RADIUS
        play_y = height - 1.5 * RADIUS
        play_x = play_x + 2.5 * RADIUS

    pygame.display.update()


def drop_piece(board, row, col, piece):
    """ The function `drop_piece` takes in a board, a row, a column, and a piece, and places the piece in the board at the
    given row and column

    :param board: the game board
    :param row: The row where the piece will be dropped
    :param col: The column where the piece is to be dropped
    :param piece: The piece you want to drop
    """
    board[row][col] = piece


def is_valid_location(board, col):
    """ If the top row of the board is empty, then the column is a valid location to place a piece

    :param board: The game board
    :param col: The column to check if it's valid
    :return: The function is_valid_location is returning the value of the last row and the column that is passed in.
    """
    return board[rows - 1][col] == 0


def get_next_open_row(board, col):
    """ **Given a column, find the next open row in that column.**

    Let's break it down

    :param board: The game board
    :param col: The column where the player wants to drop a piece
    :return: The row number of the first open space in the column.
    """
    for r in range(rows):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    """ It checks if there are four pieces in a row, either horizontally, vertically, or diagonally

    :param board: The game board
    :param piece: The piece that we are checking for a win
    :return: True or False
    """
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
    """ It creates a menu with three buttons, one for single player, one for two player, and one for the rules.
    """
    while True:
        screen.blit(BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # Button size
        button_width = width / 5
        button_height = height / 15
        button_x = width / 2

        # buttons
        # single player button
        single_y = height / 2.7

        single_button = Button(button_x, single_y, button_width, button_height)

        if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                and (single_y - (button_height / 2)) <= mouse[1] <= (single_y + (button_height / 2)):
            single_button.draw(screen, DARK_WHITE, 0, 0, "monospace", 40, WHITE, 'One-Player')
        single_button.draw(screen, WHITE, 1, 0, 'monospace', 40, WHITE, 'One-Player')

        # two player button
        multi_y = height / 2.2

        multi_button = Button(button_x, multi_y, button_width, button_height)

        if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                and (multi_y - (button_height / 2)) <= mouse[1] <= (multi_y + (button_height / 2)):
            multi_button.draw(screen, DARK_WHITE, 0, 0, "monospace", 40, WHITE, 'Two-Player')
        multi_button.draw(screen, WHITE, 1, 0, "monospace", 40, WHITE, 'Two-Player')

        # rules button
        rules_y = height / 1.85

        rules_button = Button(button_x, rules_y, button_width, button_height)

        if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                and (rules_y - (button_height / 2)) <= mouse[1] <= (rules_y + (button_height / 2)):
            rules_button.draw(screen, DARK_WHITE, 0, 0, "monospace", 40, WHITE, 'Rules')
        rules_button.draw(screen, WHITE, 1, 0, "monospace", 40, WHITE, 'Rules')

        # quit button
        quit_y = height / 1.55
        quit_width = width / 15
        quit_height = height / 18

        quit_button = Button(button_x, quit_y, quit_width, quit_height)

        quit_button.draw(screen, LIGHT_WHITE, 0, 0, "monospace", 40, BLACK, 'Quit')
        if (button_x - (quit_width / 2)) <= mouse[0] <= (button_x + (quit_width / 2)) \
                and (quit_y - (quit_height / 2)) <= mouse[1] <= (quit_y + (quit_height / 2)):
            quit_button.draw(screen, DARK_WHITE, 0, 0, "monospace", 40, WHITE, 'Quit')

        for choice in pygame.event.get():
            if choice.type == pygame.QUIT:
                pygame.quit()

            if choice.type == pygame.MOUSEBUTTONDOWN:
                if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                        and (single_y - (button_height / 2)) <= mouse[1] <= (single_y + (button_height / 2)):
                    single()
                elif (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                        and (multi_y - (button_height / 2)) <= mouse[1] <= (multi_y + (button_height / 2)):
                    multi()
                elif (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                        and (rules_y - (button_height / 2)) <= mouse[1] <= (rules_y + (button_height / 2)):
                    rules()
                elif (button_x - (quit_width / 2)) <= mouse[0] <= (button_x + (quit_width / 2)) \
                        and (quit_y - (quit_height / 2)) <= mouse[1] <= (quit_y + (quit_height / 2)):
                    pygame.quit()

        pygame.display.update()


def evaluate_window(window, piece):
    score = 0
    opppiece = SINGLE_PIECE
    if piece == SINGLE_PIECE:
        opppiece = COMPUTER_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opppiece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(board[:, cols // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(rows):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(cols - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score Vertical
    for c in range(cols):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(rows - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    ## Score posiive sloped diagonal
    for r in range(rows - 3):
        for c in range(cols - 3):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(rows - 3):
        for c in range(cols - 3):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score


def is_terminal_node(board):
    return winning_move(board, SINGLE_PIECE) or winning_move(board, COMPUTER_PIECE) or len(
        get_value_locations(board)) == 0


def minmax(board, depth, alpha, beta, maxplayer):
    """ A function that takes in a board, depth, alpha, beta, and maxplayer. It then creates a list of possible moves and then
    chooses a random column from that list. It then loops through the list of possible moves and creates a copy of the
    board.

    :param board: the board we're working with
    :param depth: the depth of the search tree
    :param alpha: the best value that the maximizing player currently can guarantee at that level or above
    :param beta: the best value that the maximizing player currently can guarantee at this node or higher
    :param maxplayer: True if the current player is the maximizing player, False if the current player is the minimizing
    player
    """
    valid_locations = get_value_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, COMPUTER_PIECE):
                return (None, 100000000)
            elif winning_move(board, SINGLE_PIECE):
                return (None, -100000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, score_position(board, COMPUTER_PIECE))
    if maxplayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            copyofboard = board.copy()
            drop_piece(copyofboard, row, col, COMPUTER_PIECE)
            new_score = minmax(copyofboard, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            copyofboard = board.copy()
            drop_piece(copyofboard, row, col, SINGLE_PIECE)
            new_score = minmax(copyofboard, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def get_value_locations(board):
    """ It returns a list of all the valid locations on the board

    :param board: The current board state
    :return: The column number of the first empty space in the board.
    """
    valid_locations = []
    for col in range(7):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


'''def computermove(board):
    """ The computer randomly chooses a column to drop a piece in. If the column is full, it chooses another column

    :param board: The game board
    :return: The game_over variable is being returned.
    """
    # posx = event.pos[0]
    # col = int(math.floor(posx / len_piece))
    pygame.time.wait(800)
    compcol = random.randint(0, 6)
    if is_valid_location(board, compcol):
        row = get_next_open_row(board, compcol)
        pygame.mixer.Sound.play(chip_sound)
        drop_piece(board, row, compcol, 2)

        if winning_move(board, 2):
            label = heading_font.render(PLAYER_1 + " wins!!", True, YELLOW)
            screen.blit(label, (40, 10))
            game_over = True
            return game_over
'''


def single():
    """ It's a function that allows the user to play against the computer """
    while True:
        PLAYER_1 = get_player_name()

        #####################3 GET COLOR FOR PLAYER 1
        PLAYER_1_COLOR = get_player_color()

        ###################3 this makes sure user enters valid Color
        while PLAYER_1_COLOR.lower() == "yellow" or validateColors(PLAYER_1_COLOR) is False:
            PLAYER_1_COLOR = get_player_color()

        COMPUTER_NAME = "Computer"
        COMPUTER_COLOR = YELLOW
        screen.fill(LIGHT_BLUE)

        player_colors = [PLAYER_1_COLOR, COMPUTER_COLOR]
        board = create_board()
        board_gen_gui(screen, LIGHT_BLUE, board, player_colors)

        strip_w = width - (14 * RADIUS)
        strip_h = height - (15 * RADIUS)
        strip = pygame.Rect(0, 0, strip_w, strip_h)

        len_piece = strip_w / cols

        game_over = False
        exit_game = False
        turn = 0
        winner = PLAYER_1

        while not game_over:
            if turn == 0:
                whose_turn = heading_font.render(PLAYER_1 + "'s Turn", True, RED)
                head_width, head_height = heading_font.size(PLAYER_1 + "'s Turn")

            heading_y = (strip_h - head_height) / 2
            screen.blit(whose_turn, (strip_w, heading_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, LIGHT_BLUE, strip)
                    posx = event.pos[0]
                    if posx < strip_w - RADIUS:
                        if turn == 0:
                            pygame.draw.circle(screen, RED, (posx, int(height / 10)), RADIUS)
                        # else:
                        # pygame.draw.circle(screen, YELLOW, (posx, int(height / 10)), RADIUS)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # print(event.pos)
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / len_piece))
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            pygame.mixer.Sound.play(chip_sound)
                            drop_piece(board, row, col, 1)

                            if winning_move(board, 1):
                                winner = PLAYER_1
                                game_over = True

                        # Ask for Player 2 Input
                        # Computer is yellow

                        board_gen_gui(screen, LIGHT_BLUE, board, player_colors)

                        turn += 1
                        turn = turn % 2

            if turn == 1:
                # posx = event.pos[0]
                # gameresult = computermove(board)
                pygame.time.wait(500)
                col, minmaxscore = minmax(board, 5, -math.inf, math.inf, True)

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    pygame.mixer.Sound.play(chip_sound)
                    drop_piece(board, row, col, COMPUTER_PIECE)

                    if winning_move(board, COMPUTER_PIECE):
                        label = heading_font.render(PLAYER_1 + " wins!!", True, YELLOW)
                        screen.blit(label, (40, 10))
                        winner = COMPUTER_NAME
                        game_over = True

                    board_gen_gui(screen, LIGHT_BLUE, board, player_colors)

                    turn += 1
                    turn = turn % 2

            pygame.display.update()

            # end the game

        if game_over:
            while not exit_game:
                display_winner(winner)
                check_restart("single")


def display_winner(winner):
    """ It displays the winner's name on the screen for 3 seconds

    :param winner: The winner of the game
    """

    label = heading_font.render(winner + " wins!!", True, YELLOW)

    # game win sound
    mixer.music.load("game_win.wav")
    mixer.music.play()

    screen.blit(label, (40, 10))
    pygame.display.update()
    pygame.time.wait(3000)


def multi():
    """ It creates a board, displays it on the screen, and then allows the players to play the game """
    # this function is for multiplayer mode of the game where two players can play against each other
    # this function is called when the user clicks on the multiplayer button on the main menu
    while True:
        player_one_text_box, player_two_text_box = create_text_boxes()
        PLAYER_1, PLAYER_2 = get_player_names(player_one_text_box, player_two_text_box)

        player_one_color_box, player_two_color_box = create_color_boxes()
        PLAYER_1_COLOR, PLAYER_2_COLOR = get_player_colors(player_one_color_box, player_two_color_box)

        ################### THIS MAKES SURE PLAYERS ENTER VALID COLORS
        while PLAYER_1_COLOR == PLAYER_2_COLOR or validateColors(PLAYER_1_COLOR) is False or validateColors(
                PLAYER_2_COLOR) is False:
            player_one_color_box, player_two_color_box = create_color_boxes()
            PLAYER_1_COLOR, PLAYER_2_COLOR = get_player_colors(player_one_color_box, player_two_color_box)

        player_colors = [PLAYER_1_COLOR, PLAYER_2_COLOR]
        board = create_board()
        board_gen_gui(screen, BLUE, board, player_colors)

        strip_w = width - (14 * RADIUS)
        strip_h = height - (15 * RADIUS)
        strip = pygame.Rect(0, 0, strip_w, strip_h)

        len_piece = strip_w / cols

        game_over = False
        exit_game = False
        turn = 0
        winner = PLAYER_1

        while not game_over:
            if turn == 0:
                whose_turn = heading_font.render(PLAYER_1 + "'s Turn", True, PLAYER_1_COLOR)
                head_width, head_height = heading_font.size(PLAYER_1 + "'s Turn")
            else:
                whose_turn = heading_font.render(PLAYER_2 + "'s Turn", True, PLAYER_2_COLOR)
                head_width, head_height = heading_font.size(PLAYER_2 + "'s Turn")

            heading_y = (strip_h - head_height) / 2
            screen.blit(whose_turn, (strip_w, heading_y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLUE, strip)
                    posx = event.pos[0]
                    if posx < strip_w - RADIUS:
                        if turn == 0:
                            pygame.draw.circle(screen, PLAYER_1_COLOR, (posx, int(height / 10)), RADIUS)
                        else:
                            pygame.draw.circle(screen, PLAYER_2_COLOR, (posx, int(height / 10)), RADIUS)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / len_piece))
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            pygame.mixer.Sound.play(chip_sound)
                            drop_piece(board, row, col, 1)

                            if winning_move(board, 1):
                                display_winner(winner)
                                game_over = True

                    # Ask for Player 2 Input
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / len_piece))
                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            pygame.mixer.Sound.play(chip_sound)
                            drop_piece(board, row, col, 2)

                            if winning_move(board, 2):
                                winner = PLAYER_2
                                game_over = True

                    board_gen_gui(screen, BLUE, board, player_colors)

                    turn += 1
                    turn = turn % 2

                    if game_over:
                        pygame.time.wait(500)

            pygame.display.update()

        if game_over:
            while not exit_game:
                display_winner(winner)
                check_restart("multi")


def rules():
    """ This function displays the rules of the game to the player """
    while True:
        # filling the background
        screen.fill(LIGHT_BLUE)

        # Rules titles
        rules_title_font = pygame.font.SysFont('freesansbold', 100)
        rulesText = rules_title_font.render("RULES", True, WHITE)
        title_width, title_height = rules_title_font.size('RULES')
        title_x = (width - title_width) / 2

        # Listed Rules
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

        # Outputting all text
        text_width, text_height = rules_font.size(rule1)
        text_y = height / 3.5

        screen.blit(rulesText, (title_x, height / 10))
        screen.blit(text1, (width / 100, text_y))
        screen.blit(text2, (width / 100, text_y + 2 * text_height))
        screen.blit(text3, (width / 100, text_y + 4 * text_height))
        screen.blit(text4, (width / 100, text_y + 6 * text_height))
        screen.blit(text5, (width / 100, text_y + 8 * text_height))

        # Back Button
        mouse = pygame.mouse.get_pos()

        for click in pygame.event.get():
            if click.type == pygame.QUIT:
                pygame.quit()

            if click.type == pygame.MOUSEBUTTONDOWN:
                if back_x <= mouse[0] <= back_x + back_width and back_y <= mouse[1] <= back_y + back_height:
                    main_menu()

        back_width, back_height = rules_font.size("back")
        back_x = (width - back_width) / 2
        back_y = 4 * height / 5

        back = rules_font.render("Back", True, WHITE)
        if back_x <= mouse[0] <= back_x + back_width and back_y <= mouse[1] <= back_y + back_height:
            back = rules_font.render("Back", True, DARK_WHITE)
        screen.blit(back, (back_x, back_y))

        pygame.display.update()


def get_player_name():
    """ It creates a text box and waits for the user to enter text

    :return: The text that the user inputs.
    """
    text_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    prompt = font.render('Enter your name: or close the window to quit', True, WHITE)

    active = False
    text = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if text_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill(LIGHT_BLUE)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        text_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (text_box.x + 5, text_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, text_box, 2)

        screen.blit(prompt, (100, 50))

        pygame.display.flip()
        pygame.display.update()
    return text


################################################ NEW CODE ADDED HERE TO GET COLOR FOR SINGLE PLAYER ###############################
def get_player_color():
    """ It creates a text box and waits for the user to enter text

    :return: The text that the user inputs.
    """
    text_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    prompt = font.render('Enter your Color: or close the window to quit', True, WHITE)

    active = False
    text = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if text_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill(LIGHT_BLUE)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        text_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (text_box.x + 5, text_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, text_box, 2)

        screen.blit(prompt, (100, 50))

        pygame.display.flip()
        pygame.display.update()
    return text


################################################### END OF SINGLE PLAYER GET COLOR METHOD ############################3

def create_text_boxes():
    """ It creates two text boxes and returns them

    :return: The player_one_text_box and player_two_text_box are being returned.
    """
    screen.fill(BLUE)

    # text box for player one
    player_one = font.render("Player One: ", True, WHITE)
    player_one_rect = player_one.get_rect()
    player_one_rect.center = (width / 2.5, height / 2.5)
    screen.blit(player_one, player_one_rect)

    # text box for player two
    player_two = font.render("Player Two: ", True, WHITE)
    player_two_rect = player_two.get_rect()
    player_two_rect.center = (width / 2.5, height / 2)
    screen.blit(player_two, player_two_rect)

    # create text boxes
    player_one_text_box = pygame.Rect(width / 2, height / 2.5, 200, 50)
    player_two_text_box = pygame.Rect(width / 2, height / 2, 200, 50)

    # draw text boxes
    pygame.draw.rect(screen, WHITE, player_one_text_box, 2)
    pygame.draw.rect(screen, WHITE, player_two_text_box, 2)

    return player_one_text_box, player_two_text_box


#######################             changes made here for adding color boxes                      ################################3
def create_color_boxes():
    """ It creates two text boxes and returns them

    :return: The player_one_text_box and player_two_text_box are being returned.
    """
    screen.fill(BLUE)

    # text box for player one
    player_one = font.render("Color for Player One: ", True, WHITE)
    player_one_rect = player_one.get_rect()
    player_one_rect.center = (width / 2.5, height / 2.5)
    screen.blit(player_one, player_one_rect)

    # text box for player two
    player_two = font.render("Color for Player Two: ", True, WHITE)
    player_two_rect = player_two.get_rect()
    player_two_rect.center = (width / 2.5, height / 2)
    screen.blit(player_two, player_two_rect)

    # create text boxes
    player_one_text_box = pygame.Rect(width / 2, height / 2.5, 200, 50)
    player_two_text_box = pygame.Rect(width / 2, height / 2, 200, 50)

    # draw text boxes
    pygame.draw.rect(screen, WHITE, player_one_text_box, 2)
    pygame.draw.rect(screen, WHITE, player_two_text_box, 2)

    return player_one_text_box, player_two_text_box


def get_player_colors(player_one_text_box, player_two_text_box):
    """ It takes in two text boxes and returns the names of the players

    :param player_one_text_box: The rectangle that the player one text will be displayed in
    :param player_two_text_box: The rectangle that the player two text will be displayed in
    :return: the player names.
    """
    prompt = font.render("Player 1 type in your Color then press enter to enter player 2's Color", True, WHITE)
    screen.blit(prompt, (100, 50))

    player_one_name = ""
    player_two_name = ""

    player_one_name_entered = False
    player_two_name_entered = False

    while not player_one_name_entered or not player_two_name_entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not player_one_name_entered:
                        player_one_name_entered = True
                    elif not player_two_name_entered:
                        player_two_name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    if not player_one_name_entered:
                        player_one_name = player_one_name[:-1]
                    elif not player_two_name_entered:
                        player_two_name = player_two_name[:-1]
                else:
                    if not player_one_name_entered:
                        player_one_name += event.unicode
                    elif not player_two_name_entered:
                        player_two_name += event.unicode

        # draw text boxes
        pygame.draw.rect(screen, WHITE, player_one_text_box, 2)
        pygame.draw.rect(screen, WHITE, player_two_text_box, 2)

        # draw text
        player_one_text = font.render(player_one_name, True, WHITE)
        player_two_text = font.render(player_two_name, True, WHITE)

        screen.blit(player_one_text, player_one_text_box)
        screen.blit(player_two_text, player_two_text_box)

        color = WHITE

        prompt = font.render("Close the window to quit and enter to continue", True, color)

        screen.blit(prompt, (width / 2, height / 1.5))

        pygame.display.update()

    return player_one_name, player_two_name


######################### Ended here CODES FOR GETTING COLOR BOXES, AND CHOICE COLORS ###########################################

def get_player_names(player_one_text_box, player_two_text_box):
    """ It takes in two text boxes and returns the names of the players

    :param player_one_text_box: The rectangle that the player one text will be displayed in
    :param player_two_text_box: The rectangle that the player two text will be displayed in
    :return: the player names.
    """
    prompt = font.render("Player 1 type in your name then press enter to enter player 2's name", True, WHITE)
    screen.blit(prompt, (100, 50))

    player_one_name = ""
    player_two_name = ""

    player_one_name_entered = False
    player_two_name_entered = False

    while not player_one_name_entered or not player_two_name_entered:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not player_one_name_entered:
                        player_one_name_entered = True
                    elif not player_two_name_entered:
                        player_two_name_entered = True
                elif event.key == pygame.K_BACKSPACE:
                    if not player_one_name_entered:
                        player_one_name = player_one_name[:-1]
                    elif not player_two_name_entered:
                        player_two_name = player_two_name[:-1]
                else:
                    if not player_one_name_entered:
                        player_one_name += event.unicode
                    elif not player_two_name_entered:
                        player_two_name += event.unicode

        # draw text boxes
        pygame.draw.rect(screen, WHITE, player_one_text_box, 2)
        pygame.draw.rect(screen, WHITE, player_two_text_box, 2)

        # draw text
        player_one_text = font.render(player_one_name, True, WHITE)
        player_two_text = font.render(player_two_name, True, WHITE)

        screen.blit(player_one_text, player_one_text_box)
        screen.blit(player_two_text, player_two_text_box)

        color = WHITE

        prompt = font.render("Close the window to quit and enter to continue", True, color)

        screen.blit(prompt, (width / 2, height / 1.5))

        pygame.display.update()

    return player_one_name, player_two_name


def check_restart(game_type):
    """ It's a function that asks the user if they want to continue or exit the game

    :param game_type: This is the type of game that was being played
    """
    decided = False
    while not decided:
        screen.blit(BG, (0, 0))
        mouse = pygame.mouse.get_pos()

        # Button size
        button_width = width / 5
        button_height = height / 15
        button_x = width / 2

        # buttons
        # Play again button
        play_y = height / 2.7

        play_button = Button(button_x, play_y, button_width, button_height)

        if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                and (play_y - (button_height / 2)) <= mouse[1] <= (play_y + (button_height / 2)):
            play_button.draw(screen, DARK_WHITE, 0, 0, "monospace", 40, WHITE, 'Play Again')
        play_button.draw(screen, WHITE, 1, 0, 'monospace', 40, WHITE, 'Play Again')

        # Back to main menu button
        return_y = height / 2.2

        return_button = Button(button_x, return_y, button_width, button_height)

        if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                and (return_y - (button_height / 2)) <= mouse[1] <= (return_y + (button_height / 2)):
            return_button.draw(screen, DARK_WHITE, 0, 0, "monospace", 40, WHITE, 'Main Menu')
        return_button.draw(screen, WHITE, 1, 0, 'monospace', 40, WHITE, 'Main Menu')

        # Exit button
        exit_y = height / 1.85

        exit_button = Button(button_x, exit_y, button_width, button_height)

        if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                and (exit_y - (button_height / 2)) <= mouse[1] <= (exit_y + (button_height / 2)):
            exit_button.draw(screen, DARK_WHITE, 0, 0, "monospace", 40, WHITE, 'Exit')
        exit_button.draw(screen, WHITE, 1, 0, "monospace", 40, WHITE, 'Exit')

        for choice in pygame.event.get():
            if choice.type == pygame.QUIT:
                pygame.quit()
                quit()
            if choice.type == pygame.MOUSEBUTTONDOWN:
                if (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                        and (play_y - (button_height / 2)) <= mouse[1] <= (play_y + (button_height / 2)):
                    decided = True
                    if game_type == "single":
                        single()
                    elif game_type == "multi":
                        multi()
                elif (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) and \
                        (return_y - (button_height / 2)) <= mouse[1] <= (return_y + (button_height / 2)):
                    main_menu()
                elif (button_x - (button_width / 2)) <= mouse[0] <= (button_x + (button_width / 2)) \
                        and (exit_y - (button_height / 2)) <= mouse[1] <= (exit_y + (button_height / 2)):
                    decided = True
                    pygame.quit()
                    quit()
                else:
                    pass

        pygame.display.update()


if __name__ == "__main__":
    # Initializing the pygame module.
    pygame.init()
    pygame.mixer.init()

    # sound for chips
    chip_sound = pygame.mixer.Sound('gameSound.wav')
    # sound for enter game
    mixer.music.load("entrance.wav")
    mixer.music.play()
    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    LIGHT_BLUE = (0, 100, 255)
    LIGHT_WHITE = (170, 170, 170)
    DARK_WHITE = (100, 100, 100)
    GREEN = (0, 255, 0)

    PLAYER_1 = "Player 1"
    PLAYER_2 = "Player 2"
    ##################333 default player colors
    PLAYER_1_COLOR = YELLOW
    PLAYER_2_COLOR = RED
    player_colors = [RED, YELLOW]  ##############3 CHANGES MADE HERE

    # define our screen size
    # SQUARESIZE = 100

    EMPTY = 0
    FIRST_PIECE = 1
    SECOND_PIECE = 2
    SINGLE_PIECE = 1
    COMPUTER_PIECE = 2

    WINDOW_LENGTH = 4

    # Screen
    width = 1280
    height = 720
    res = (width, height)
    screen = pygame.display.set_mode(res)

    BG = pygame.image.load("Dots.jpeg")
    BG = pygame.transform.scale(BG, res)
    heading_font = pygame.font.SysFont("monospace", 50)
    FIRST_PIECE = 1
    SECOND_PIECE = 2

    # chips ratio to screen
    if width > height:
        RADIUS = int(height / 18)
    else:
        RADIUS = int(width / 18)

    rows = 6
    cols = 7

    font = pygame.font.SysFont('Calibri', 25, True, False)

    main_menu()

    pygame.quit()
