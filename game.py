from pickle import FALSE
import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center,60, 5)

def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

def display_game_screen():
    print("game start")

pygame.init()
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Chimpanzee Game")


start_button = pygame.Rect(0,0,120,120)
start_button.center = (120,screen_height-120)

BLACK = (0,0,0)
WHITE = (255,255,255)

start = False

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