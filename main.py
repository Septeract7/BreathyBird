import pygame
from pygame.locals import *

# setup pygame
pygame.init()

#fix framerate
gameclock = pygame.time.Clock()
fps = 60

screen_width = 765
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("BreathyBird💨")

# load images
bg = pygame.image.load('img/bg_1.png')
ground = pygame.image.load('img/ground.jpg')
bird = pygame.image.load('img/bird1_wingsup.png')

# game variables
scroll_distance = 0
scroll_speed = 4    # scroll 4 pixels per tick

bird_x_pos = 100
bird_y_pos = 340

# main game loop
run = True
while run:

    gameclock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(bg, (0,0))
    screen.blit(ground, (scroll_distance,680))
    scroll_distance = scroll_distance - scroll_speed
    if abs(scroll_distance) >= screen_width:
        scroll_distance = 0

    screen.blit(bird, (bird_x_pos, bird_y_pos))

    pygame.display.update()


pygame.quit()