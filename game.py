import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center,60, 5)

pygame.init()
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Chimpanzee Game")


start_button = pygame.Rect(0,0,120,120)
start_button.center = (120,screen_height-120)

BLACK = (0,0,0)
WHITE = (255,255,255)

running = True
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    display_start_screen()
    pygame.display.update()
pygame.quit()