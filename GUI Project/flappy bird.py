import pygame  # importing pygame
import sys  # importing sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
speed = pygame.time.Clock()
# adding loop to make pygame work until whe user wants to quit
while True:
    pygame.display.update()
    speed.tick(150)
    for movement in pygame.event.get():
        if movement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
