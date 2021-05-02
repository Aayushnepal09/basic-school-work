import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
speed = pygame.time.Clock()

while True:
    for movement in pygame.movement.get():
        if movement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
