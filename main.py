import pygame
from pygame.locals import*
pygame.init()
clock = pygame.time.Clock()
fps = 60


screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('flappy bird')

# load images
bg = pygame.image.load('bg.png') # leads bg
ground_img = pygame.image.load('ground.png')# loads ground
#variables
ground_scroll = 0
scroll_speed = 0.4 
run = True
while run:
    clock.tick(fps)
    #draw bg
    screen.blit(bg, (0, -100))
   
#draw and scroll grounf
    screen.blit(ground_img, (ground_scroll, 500))
    ground_scroll -= scroll_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
