import pygame
import sys
import random

pygame.init()

# window
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# color
black = (0, 0, 0)

#basic setting
distance = 5
FPS = 60
clock = pygame.time.Clock()

# fish
fish_img = pygame.image.load("images/fish.png")
fish_rect = fish_img.get_rect()
fish_rect.center = (320, 400)
fliped_fish = pygame.transform.flip(fish_img, True, False)

# heart
heart_img = pygame.image.load("images/life.png")
heart_rect = heart_img.get_rect()
heart_rect.centerx = (random.randint(50, 590))
heart_rect.centery = 20

# bugs
bug_one_img = pygame.image.load("images/bug_one.png")
bug_one_rect = bug_one_img.get_rect()
bug_one_rect.centerx = (random.randint(50, 590))
bug_one_rect.centery = 20

bug_two_img = pygame.image.load("images/bug_two.png")
bug_two_rect = bug_one_img.get_rect()
bug_two_rect.centerx = (random.randint(50, 590))
bug_two_rect.centery = 20

# background
bg_img = pygame.image.load("images/background.jpg")
bg_rect = bg_img.get_rect()
bg_rect.center = (100 ,200)

# main cycle
run = True
while run:
    

    # update screen fill with black color
    SCREEN.fill(black)

    # background
    SCREEN.blit(bg_img, bg_rect)

    # heart
    SCREEN.blit(heart_img, heart_rect)

    # bugs
    SCREEN.blit(bug_one_img, bug_one_rect)
    SCREEN.blit(bug_two_img, bug_two_rect)
    
    # keys get pressed
    keys = pygame.key.get_pressed()

    # heart movement
    if heart_rect.centery <= 600:
        heart_rect.centery += 5

    # bugs movement
    if bug_one_rect.centery <= 600:
        bug_one_rect.centery += 5

    if bug_two_rect.centery <= 600:
        bug_two_rect.centery += 5

    # fish movement
    if keys[pygame.K_LEFT] and fish_rect.centerx >= 50:
        SCREEN.blit(fish_img, fish_rect)
        fish_rect.centerx -= distance

    if keys[pygame.K_RIGHT] and fish_rect.centerx <= 590: 
        SCREEN.blit(fliped_fish, fish_rect)
        fish_rect.centerx += distance
    else:
        SCREEN.blit(fish_img, fish_rect) 

    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    

    # slowdown cycle
    clock.tick(FPS)

    #update screen
    pygame.display.update()

pygame.quit()

