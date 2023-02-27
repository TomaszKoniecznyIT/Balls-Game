import pygame   # importing game modules
import random   # importing the randomizing module


pygame.init() # initialization of game modules

# creating a window with a resolution of 800 by 600 pixels
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Ball-Game") # name on the bar

# preparation of 3 fonts
txt1 = pygame.font.Font("freesansbold.ttf", 32)
txt2 = pygame.font.Font("freesansbold.ttf", 24)
txt3 = pygame.font.Font("freesansbold.ttf", 64)

# I set 7 colors in the dictionary
colors_balls = {1: (254, 254, 0), 2: (0, 128, 0), 3: (255, 128, 0), 4: (128, 0, 0), 5: (0, 0, 255), 6: (237, 19, 19), 7: (255, 0, 255)}

color_list = [] # I create an empty list in which the colors will be held

# variables to save results
score = 0
best_score = 0

running = True


# the function draws the lines of the game board
def board_lines():
    # horizontal and vertical line
    vertical_line = pygame.Surface([1, 540])
    horizontal_line = pygame.Surface([540, 1])
    # color fill
    vertical_line.fill((255, 255, 255))
    horizontal_line.fill((255, 255, 255))
    # start coordinates
    x = 230
    y = 30
    
    xy_move = 60 # move by px
    
    # draw 10 horizontal lines (xy_move - distance)
    for _ in range(10):
        screen.blit(vertical_line, (x,y))
        x += xy_move    
    
    x = 230 # after the loop you need to reset x to the initial setting
    
    # draw 10 vertical lines (xy_move - distance)
    for _ in range(10):
        screen.blit(horizontal_line, (x,y))
        y += xy_move


# the function draws the lines for next 3 balls
def next_balls_lines():
    # horizontal and vertical line
    horizontal_line = pygame.Surface([180, 1])
    vertical_line = pygame.Surface([1, 60])
    # color fill
    vertical_line.fill((255, 255, 255))
    horizontal_line.fill((255, 255, 255))
    # start coordinates
    x= 10
    y=200

    # draw a lines
    screen.blit(horizontal_line, (x, y))
    screen.blit(horizontal_line, (x, y + 60))
    screen.blit(vertical_line, (x, y))
    screen.blit(vertical_line, (x + 60, y))
    screen.blit(vertical_line, (x + 120, y))
    screen.blit(vertical_line, (x + 180, y))


# function creating the reset button
def reset_box():
    # drawing a reset button in color
    box_reser = pygame.Surface([160, 55])
    box_reser.fill((165, 208, 232))
    screen.blit(box_reser, (20,350))
    # adding text to the button
    reset_txt = txt2.render("R - RESET", True, (59, 32, 212))
    screen.blit(reset_txt, (40, 365))


# function creating rectangle with result
def score_box():
    # drawing a rectangle with result
    box_score = pygame.Surface([160, 110])
    box_score.fill((165, 208, 232))
    screen.blit(box_score, (20, 30))
    # adding text and current score 
    score_txt_1 = txt1.render("SCORE", True, (59, 32, 212))
    screen.blit(score_txt_1, (42, 40))
    score_txt_2 = txt1.render(str(score), True, (59, 32, 212))
    screen.blit(score_txt_2, (30, 100))


# function creating rectangle with the best score
def the_best_score_box():
    # drawing a rectangle with the best score
    box_score = pygame.Surface([160, 110])
    box_score.fill((165, 208, 232))
    screen.blit(box_score, (20, 450))
     # adding text and the best score
    score_txt_1 = txt1.render("THE BEST", True, (59, 32, 212))
    screen.blit(score_txt_1, (40, 455))
    score_txt_2 = txt1.render("SCORE", True, (59, 32, 212))
    screen.blit(score_txt_2, (58, 480))
    score_txt_3 = txt1.render(str(best_score), True, (59, 32, 212))
    screen.blit(score_txt_3, (30, 520))


# function drawing a line separating the game board from the results
def line_score():
    line_score = pygame.Surface([3, 600])
    screen.blit(line_score, (200, 0))


# function drawing board
def board():
    screen_game = pygame.Surface([540, 540])
    screen_game.fill((166, 193, 237))
    screen.blit(screen_game, (230, 30))


# creating a 9 x 9 matrix to hold for the state of the board (filled with zeros at the start)
def matrix_start():
    start_matrix = []
    matrX = []
    for _ in range(9):
        for _ in range(9):
            matrX.append(0)
        start_matrix.append(matrX)
        matrX = []
    return start_matrix


# game loop 
while running:
    screen.fill((208, 236, 245)) # filling with color
    # calling drawing functions
    line_score()
    board()
    board_lines()
    next_balls_lines()
    reset_box()
    score_box()
    the_best_score_box()