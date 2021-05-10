import random

import pygame
# initialize pygame
pygame.init()
# Create the screen
screen = pygame.display.set_mode((800,800))
# title and icon
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('enemy.png')
pygame.display.set_icon(icon)
# Adding player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

#adding enemy
enemyImag=pygame.image.load('enemy.png')
enemyX=random.randint(0,800)
enemyy=random.randint(50,150)

# x and y coordinate passed
def player(x,y):
    #blit --> draw
    screen.blit(playerImg, (x,y))
def enemy(x,y):
    #blit---->draw
    screen.blit(enemyImag,(x,y))

# Game loop
running = True
while running:
    # RGB COLOR TO RGB for background color
    screen.fill((58, 0, 28))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Increase to 0.3 if u want to increase the speed
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    # Creating boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


  #creating bound
    player(playerX, playerY)
    enemy(enemyX,enemyy)
    pygame.display.update()
