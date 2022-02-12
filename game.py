from random import *
from tkinter.messagebox import NO
import pygame

def setup(level):
    view_count = (level//3) + 5
    view_count = min(view_count, 30)
    shuffle_grid(view_count)
    

def shuffle_grid(count):
    rows = 5
    columns = 9
    cell_size = 130
    button_size = 120
    screen_left_margin = 18
    screen_top_margin = 20
    
    grid = [[0 for i in range(columns)] for j in range(rows)]
    number = 1
    while(number <= count):
        row_index = randrange(0, rows)
        col_index = randrange(0, columns)
        if grid[row_index][col_index] == 0:
            grid[row_index][col_index] = number
            number+=1
            
            center_x = screen_left_margin + (col_index * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_index * cell_size) + (cell_size / 2)
            number_button = pygame.Rect(0,0,button_size,button_size)
            number_button.center = (center_x, center_y)
            
            number_button_list.append(number_button)
            

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center,60, 5)

def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

def display_game_screen():
    for idx, rect in enumerate(number_button_list, start=1):
        pygame.draw.rect(screen, GRAY, rect)
        
        text = game_font.render(str(idx), True, WHITE)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text,text_rect)

pygame.init()
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Chimpanzee Game")
game_font = pygame.font.Font(None, 120)

start_button = pygame.Rect(0,0,120,120)
start_button.center = (120,screen_height-120)

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (50, 50, 50)

number_button_list = []

start = False

setup(1)


running = True
while(running):
    click_pos = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()   
            print(click_pos)
    screen.fill(BLACK)
    
    if start:
        display_game_screen()
    else:
        display_start_screen()
    if click_pos:
        check_buttons(click_pos)
        
    pygame.display.update()
    
pygame.quit()