import pygame
import sys

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


# background
bg_img = pygame.image.load("images/background.jpg")
bg_rect = bg_img.get_rect()
bg_rect.center = (200 ,200)

# main cycle
run = True
while run:
    

    # update screen fill with black color
    SCREEN.fill(black)

    # background
    SCREEN.blit(bg_img, bg_rect)
    
    # keys get pressed
    keys = pygame.key.get_pressed()

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

