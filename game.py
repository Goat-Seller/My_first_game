import pygame

# import time

# screen_set
screen_size = [1680, 1050]
screen = pygame.display.set_mode(screen_size)

# FPS function load
frames = pygame.time.Clock()

#  variables
planets = ['images/planet001.png', 'images/planet002.png', 'images/planet003.png']
p_i = 0
planet = pygame.image.load(planets[p_i])
spaceship = pygame.image.load('images/spaceship001.png')
bullet = pygame.image.load('images/bullet.png')
background = pygame.image.load('images/background.jpg')  # load image
loop = True
p_m = 590
m_d = 'r'
b_y = 900
fire = False
count = 0
s_m = 640

# keyboard handler
pygame.event.get()
keys = pygame.key.get_pressed()

# 840 640
while loop:
    screen.blit(background, [0, 0])  # transfer image to block - blit
    screen.blit(planet, [p_m, -100])
    screen.blit(bullet, [s_m+140, b_y])
    screen.blit(spaceship, [s_m, 700])
    pygame.event.get()
    keys = pygame.key.get_pressed()

    #  game_exiting
    if keys[pygame.K_ESCAPE]:
        exit()
    #  planet_movement
    if m_d == 'r':
        p_m += 5
        if p_m >= 1180:
            m_d = 'l'
    else:
        p_m -= 5
        if p_m <= 0:
            m_d = 'r'
    #  bullet_movement
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        fire = True
    if fire:
        b_y -= 10
        if b_y <= 0:
            fire = False
            b_y = 700
    #  spaceship_movement
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        move = True
        if -200 > s_m:
            move = False
            s_m = -200
        elif 1480 < s_m:
            move = False
            s_m = 1480
        else:
            s_m -= 3
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        move = True
        if -200 > s_m:
            move = False
            s_m = -200
        elif 1480 < s_m:
            move = False
            s_m = 1480
        else:
            s_m += 3

    # hit
    if b_y <= 500 and s_m <= p_m + 500 and not s_m > p_m+200 and not s_m < p_m-200:
        count += 1
        if count >= 100:
            p_i += 1
            if p_i < len(planets):
                planet = pygame.image.load(planets[p_i])
                count = 0
                p_m = 0
            elif p_i == len(planets):
                print("You've won the game!")
                loop = False

    pygame.display.update()  # refresh
    frames.tick(144)  # FPS
