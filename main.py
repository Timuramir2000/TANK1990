
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.update()
icon = pygame.image.load('images/tank1.png')
pygame.display.set_caption("TANK1990")

# Import image
imgBrick = pygame.image.load('images/block_brick.png')
imgTanks = [
    pygame.image.load('images/tank1.png'),
    pygame.image.load('images/tank2.png'),
    pygame.image.load('images/tank3.png'),
    pygame.image.load('images/tank4.png'),
    pygame.image.load('images/tank5.png'),
    pygame.image.load('images/tank6.png'),
    pygame.image.load('images/tank7.png'),
    pygame.image.load('images/tank8.png'),
    ]
imgBangs = [
    pygame.image.load('images/bang1.png'),
    pygame.image.load('images/bang2.png'),
    pygame.image.load('images/bang3.png'),
    ]
imgBonuses = [
    pygame.image.load('images/bonus_star.png'),
    pygame.image.load('images/bonus_tank.png'),
    ]

# Import sounds
sounds = [
    pygame.mixer.Sound('sounds/dead.wav'),
    pygame.mixer.Sound('sounds/destroy.wav'),
    pygame.mixer.Sound('sounds/engine.wav'),
    pygame.mixer.Sound('sounds/level_finish.mp3'),
    pygame.mixer.Sound('sounds/level_start.mp3'),
    pygame.mixer.Sound('sounds/live.wav'),
    pygame.mixer.Sound('sounds/move.wav'),
    pygame.mixer.Sound('sounds/shot.wav'),
    pygame.mixer.Sound('sounds/shot.wav'),
          ]


gameplay = True
while gameplay:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay = False
            pygame.quit()
