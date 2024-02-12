import pygame
import sys

pygame.init()

# window
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#color
black = (0, 0, 0)

#basic setting
distance = 5

# fish
fish_img = pygame.image.load("images/fish.png")
fish_rect = fish_img.get_rect()
fish_rect.center = (320, 420)


run = True
while run:
    keys = pygame.key.get_pressed()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    if keys[pygame.K_LEFT] and fish_rect.centerx >= 50:
        fish_rect.centerx -= distance
    if keys[pygame.K_RIGHT] and fish_rect.centerx <= 590:
        fish_rect.centerx += distance
        

    SCREEN.fill(black)
    SCREEN.blit(fish_img, fish_rect)

    pygame.display.update()

pygame.quit()

