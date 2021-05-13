import pygame  # importing pygame
import sys  # importing sys

# initialize pygame
pygame.init()

# creating a screen
screen = pygame.display.set_mode((500, 500))

# title and icon
pygame.display.set_caption("FLAPPY BIRD")
icon = pygame.image.load('redbird-upflap.png')
pygame.display.set_icon(icon)
# Adjusting game speed
speed = pygame.time.Clock()
# adding background image
background = pygame.image.load('background-day.png')
background = pygame.transform.scale(background, (500, 500))
# adding flore image
floor = pygame.image.load('base.png')
floor = pygame.transform.scale2x(floor)
floorX = 0

def floor_movement():
    screen.blit(floor, (floorX, 400))
    screen.blit(floor, (floorX+500, 400))





# game loop
while True:

    pygame.display.update()
    speed.tick(150)
    for movement in pygame.event.get():
        if movement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    floorX -= 1
    floor_movement()
    if floorX<=-500:
        floorX=0
