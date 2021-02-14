import pygame
import sys
import numpy as np
import time

pygame.init()

HEIGHT, WIDTH = 600, 600
TITLE = "Tic Tac Toe"
BG_COLOR = (65, 163, 160)
LINE_COLOR = (23, 145, 135)
LINE_WIDTH = 15
X_COLOR = (33, 32, 33)
O_COLOR = (209, 209, 209)
WINNING_LINE_WIDTH = 20

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( TITLE )
screen.fill(BG_COLOR)

board = np.zeros((3, 3))


def draw_lines():
    # vertical 1
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # vertical 2
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)
    # horizontal 1
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # horizontal 2
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

draw_lines()

player = 1

def start():
    return False

game_over = start()

def mark_square(row, column, player):
    board[row][column] = player
    if player % 2:
        draw_x(row, column)
    else:
        draw_o(row, column)

def availabe_square(row, column):
    return board[row][column] == 0

def is_board_full():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    # vertical win
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            print("vertical win!")
            draw_vertical_winning_line(col, player)
            return True

    # horizontal win
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            print("horizontal win!")
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_asc_diagonal(player)
        return True
    
    # desc diagonal win
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_desc_diagonal(player)
        return True

    return False
        


def draw_vertical_winning_line(col, player):
    x_pos = col * 200 + 100

    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = O_COLOR

    pygame.draw.line(screen, color, (x_pos, 15), (x_pos, HEIGHT - 15), WINNING_LINE_WIDTH)

def draw_horizontal_winning_line(row, player):
    y_pos = row * 200 + 100
    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = O_COLOR

    pygame.draw.line(screen, color, (15, y_pos), (WIDTH - 15, y_pos), WINNING_LINE_WIDTH)

def draw_asc_diagonal(player):

    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = O_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WINNING_LINE_WIDTH)


def draw_desc_diagonal(player):

    if player == 1:
        color = X_COLOR
    elif player == 2:
        color = O_COLOR

    pygame.draw.line(screen, color, (WIDTH - 15, 15), (15, HEIGHT - 15), WINNING_LINE_WIDTH)


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(3):
        for col in range(3):
            board[row][col] = 0

def draw_x(row, column):
    #pygame.draw.line(screen, X_COLOR, (x + 75, y + 75), (x - 75, y - 75), LINE_WIDTH)
    #pygame.draw.line(screen, X_COLOR, (x - 75, y + 75), (x + 75, y - 75), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (column * 200 + 25, row * 200 + 175), (column * 200 + 175, row * 200 + 25), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (column * 200 + 175, row * 200 + 175), (column * 200 + 25, row * 200 + 25), LINE_WIDTH)

def draw_o(row, column):
    #pygame.draw.circle(screen, O_COLOR, pos, 75, LINE_WIDTH)
    pygame.draw.circle(screen, O_COLOR, (column * 200 + 100, row * 200 + 100), 75, LINE_WIDTH)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(board)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                restart()
            if event.key == pygame.K_ESCAPE:
                print(board)
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = (event.pos[0], event.pos[1])
            x, y = pos

            clicked_row = int(y // 200)
            clicked_col = int(x // 200)
            if availabe_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2
                    if check_win(1):
                        game_over = True
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1
                    if check_win(2):
                        game_over = True
    time.sleep(0.01)
    pygame.display.update()