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
FPS = 60
clock = pygame.time.Clock()

# fish
fish_img = pygame.image.load("images/fish.png")
fish_rect = fish_img.get_rect()
fish_rect.center = (320, 420)

#background
bg_img = pygame.image.load("images/background.jpg")
bg_rect = bg_img.get_rect()
bg_rect.center = (200 ,200)


run = True
while run:
    # keys get pressed
    keys = pygame.key.get_pressed()
    
    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()

    #fish movement
    if keys[pygame.K_LEFT] and fish_rect.centerx >= 50:
        fish_rect.centerx -= distance
    if keys[pygame.K_RIGHT] and fish_rect.centerx <= 590:
        fish_rect.centerx += distance
        
    # update screen fill with black color
    SCREEN.fill(black)

    # images
    SCREEN.blit(bg_img, bg_rect)
    SCREEN.blit(fish_img, fish_rect)
    

    # slowdown cycle
    clock.tick(FPS)

    #update screen
    pygame.display.update()

pygame.quit()

