import pygame
import sys
import random

pygame.init()

# window
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# color
black = (0, 0, 0)
white = (255, 255, 255)

# basic setting
distance = 8
FPS = 60
clock = pygame.time.Clock()
score_point = 0
life_point = 3

# font setting
my_font = pygame.font.SysFont("Kokila", 50)




# healt
life_img = pygame.image.load("images/life.png")
life_rect = life_img.get_rect()
life_rect.center = (80, 20)

# fish
fish_img = pygame.image.load("images/fish.png")
fish_rect = fish_img.get_rect()
fish_rect.center = (320, 400)
fliped_fish = pygame.transform.flip(fish_img, True, False)

# heart bar
heart_img = pygame.image.load("images/life.png")
heart_rect = heart_img.get_rect()
heart_rect.centerx = (random.randint(50, 590))
heart_rect.centery = (random.randint(-10000, -5000))


# bugs
bug_one_img = pygame.image.load("images/bug_one.png")
bug_one_rect = bug_one_img.get_rect()
bug_one_rect.centerx = (random.randint(50, 590))
bug_one_rect.centery = (random.randint(-45, -20))

bug_two_img = pygame.image.load("images/bug_two.png")
bug_two_rect = bug_one_img.get_rect()
bug_two_rect.centerx = (random.randint(50, 590))
bug_two_rect.centery = (random.randint(-50, -30))
# background
bg_img = pygame.image.load("images/background.jpg")
bg_rect = bg_img.get_rect()
bg_rect.center = (100 ,200)

def falling_life_point():
    global life_point
    # heart movement
    if heart_rect.centery <= 600 :
        heart_rect.centery += random.randint(1, 7)
    if heart_rect.centery >=599:
        heart_rect.centerx = (random.randint(50, 590))
        heart_rect.centery = 20
    
    if heart_rect.colliderect(fish_rect):
        heart_rect.centerx = (random.randint(50, 590))
        heart_rect.centery = 20
        life_point += 1

def falling_bugs():
    global life_point
    global score_point
    # bugs movement
    if bug_one_rect.centery <= 600:
        bug_one_rect.centery += random.randint(1, 7)
    if bug_one_rect.centery >=599:
        life_point -= 1
        bug_one_rect.centerx = (random.randint(50, 590))
        bug_one_rect.centery = 20

    if bug_two_rect.centery <= 600:
        bug_two_rect.centery += random.randint(1, 7)
    if bug_two_rect.centery >=599:
        life_point -= 1
        bug_two_rect.centerx = (random.randint(50, 590))
        bug_two_rect.centery = 20

    # buggs collision
    if fish_rect.colliderect(bug_one_rect):
        bug_one_rect.centerx = (random.randint(50, 590))
        bug_one_rect.centery = 20
        score_point += 1

    if fish_rect.colliderect(bug_two_rect):
        bug_two_rect.centerx = (random.randint(50, 590))
        bug_two_rect.centery = 20
        score_point += 1


# main cycle
run = True
while run:
    

    # update screen fill with black color
    SCREEN.fill(black)

    # background
    SCREEN.blit(bg_img, bg_rect)

    score = my_font.render(f"{score_point}", True, black)
    score_rect = score.get_rect()
    score_rect.center = (30, 22)

    life_count = my_font.render(f"{life_point}", True, black)
    life_count_rect = life_count.get_rect()
    life_count_rect.center = (110, 22)

    # images
    SCREEN.blit(heart_img, heart_rect)
    SCREEN.blit(bug_one_img, bug_one_rect)
    SCREEN.blit(bug_two_img, bug_two_rect)
    SCREEN.blit(life_img, life_rect)

    # text
    SCREEN.blit(score, score_rect)
    SCREEN.blit(life_count, life_count_rect)
    
    # keys get pressed
    keys = pygame.key.get_pressed()

    
    falling_life_point()

    falling_bugs()
    
   
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

