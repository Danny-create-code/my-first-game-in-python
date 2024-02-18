import pygame
import sys
import random

pygame.init()

# window
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nom, nom, nom")

# color
black = (0, 0, 0)

# basic setting
distance = 8
FPS = 60
clock = pygame.time.Clock()
score_point = 0
life_point = 3

current_life_point = life_point
current_score_point = score_point

# sounds
pygame.mixer.music.load("sounds/bg_sound.mp3")
pygame.mixer.music.play(-1,0.0)




# font setting
my_font = pygame.font.SysFont("Kokila", 50)


end_text = my_font.render("END GAME", True, 100)
end_text_rect = end_text.get_rect()
end_text_rect.center = 320, 240

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
heart_rect.centery = (random.randint(-45, -20))


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
    global current_life_point
    # heart's movement 
    if heart_rect.centery <= 10000 :
        heart_rect.centery += random.randint(5, 15)
    if heart_rect.centery >= 9999:
        heart_rect.centerx = (random.randint(50, 590))
        heart_rect.centery = 20
    
    # heart's collision
    if heart_rect.colliderect(fish_rect):
        heart_rect.centerx = (random.randint(50, 590))
        heart_rect.centery = 20
        current_life_point += 1
        take_life_sound = pygame.mixer.Sound("sounds/nom.mp3")
        take_life_sound.set_volume(0.4)
        take_life_sound.play()

def falling_bugs():
    global current_life_point
    global current_score_point
    # bugs's movement
    if bug_one_rect.centery <= 600:
        bug_one_rect.centery += random.randint(1, 7)
    if bug_one_rect.centery >=599:
        current_life_point -= 1
        bug_one_rect.centerx = (random.randint(50, 590))
        bug_one_rect.centery = 20

    if bug_two_rect.centery <= 600:
        bug_two_rect.centery += random.randint(1, 7)
    if bug_two_rect.centery >=599:
        current_life_point -= 1
        bug_two_rect.centerx = (random.randint(50, 590))
        bug_two_rect.centery = 20

    # buggs's collision
    if fish_rect.colliderect(bug_one_rect):
        bug_one_rect.centerx = (random.randint(50, 590))
        bug_one_rect.centery = 20
        current_score_point += 1
        take_life_sound = pygame.mixer.Sound("sounds/nom_two.mp3")
        take_life_sound.set_volume(0.4)
        take_life_sound.play()
        

    if fish_rect.colliderect(bug_two_rect):
        bug_two_rect.centerx = (random.randint(50, 590))
        bug_two_rect.centery = 20
        current_score_point += 1
        take_life_sound = pygame.mixer.Sound("sounds/nom_three.mp3")
        take_life_sound.set_volume(0.4)
        take_life_sound.play()


def end_game():
    global current_life_point
    global current_score_point
    global score_point
    global life_point
    if current_life_point == 0:
        # end game text
        
        end_sound = pygame.mixer.Sound("sounds/game_over.mp3")
        end_sound.set_volume(0.4)
        end_sound.play()
        
        SCREEN.blit(end_text, end_text_rect)
        pygame.display.update()

        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.time.wait(1000)
                    pygame.mixer.music.play(-1,0.0)
                    
                    current_score_point = score_point
                    current_life_point = life_point
                    bug_one_rect.centery = 20
                    bug_two_rect.centery = 20
                    pause = False
                elif event.type == pygame.QUIT:
                    pygame.quit()
        
        


        

        


# main cycle
run = True
while run:
    

    # update screen fill with black color
    SCREEN.fill(black)

    # background
    SCREEN.blit(bg_img, bg_rect)

    # score count
    score = my_font.render(f"{current_score_point}", True, black)
    score_rect = score.get_rect()
    score_rect.center = (30, 22)

    # life count
    life_count = my_font.render(f"{current_life_point}", True, black)
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

    end_game()
    
   
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

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                pygame.cdrom.get_paused()
    

    # slowdown cycle
    clock.tick(FPS)

    #update screen
    pygame.display.update()

pygame.quit()

