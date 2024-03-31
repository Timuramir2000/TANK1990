
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
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

turn_1: int = 180

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

# tank start coordinate
tank_coord_x = 100
tank_coord_y = 100
tank_speed = 1

# bullet start coordinate
bullets = []
bullet_coord_x = tank_coord_x
bullet_coord_y = tank_coord_yJS
gameplay = True
while gameplay:

    pygame.draw.rect(screen, (100, 100, 100), (0, 0, 100, 600,))
    pygame.draw.rect(screen, (100, 100, 100), (700, 0, 100, 600,))
    im = pygame.transform.rotate(imgTanks[1], turn_1)
    screen.blit(im, (tank_coord_x, tank_coord_y))

    keys = pygame.key.get_pressed()

    if bullets:
        for bul_in, el in enumerate(bullets):
            el.x = -12
            el.y = 0

    if keys[pygame.K_w] and tank_coord_y > 0:
        tank_coord_y -= tank_speed
        sounds[2].play()
        turn_1 = 0
    elif keys[pygame.K_s] and tank_coord_y < 568:
        tank_coord_y += tank_speed
        sounds[2].play()
        turn_1 = 180
    elif keys[pygame.K_a] and tank_coord_x > 100:
        tank_coord_x -= tank_speed
        sounds[2].play()
        turn_1 = 90
    elif keys[pygame.K_d] and tank_coord_x < 668:
        tank_coord_x += tank_speed
        sounds[2].play()
        turn_1 = -90
    else:
        sounds[2].stop()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                bullet.append[bullets]
                pygame.mixer.Channel(0).play(sounds[7])

        if event.type == pygame.QUIT:
            gameplay = False
            pygame.quit()
    pygame.display.flip()
    clock.tick(60)
    screen.fill((10, 10, 10))