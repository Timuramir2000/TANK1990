# Import main library
import pygame
# Pygame initialize
pygame.init()

# Main window parameter
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('images/tank1.png')
pygame.display.set_caption("TANK1990")

# Pygame Clock
clock = pygame.time.Clock()
bullet_image = pygame.Surface((4, 4))

# Import image
imgBrick = pygame.image.load('images/block_brick.png')

# Import player tank image
image_tank_list = [
    pygame.image.load('images/tank1.png'),
    pygame.image.load('images/tank2.png'),
    pygame.image.load('images/tank3.png'),
    pygame.image.load('images/tank4.png'),
    ]

# Import enemy tank image
image_enemy_tank_list =[
    pygame.image.load('images/enemy_tank_100.png'),
    pygame.image.load('images/enemy_tank_200.png'),
    pygame.image.load('images/enemy_tank_300.png'),
    pygame.image.load('images/enemy_tank_400.png'),
    ]

#Import explosion effect image
image_explosion_list = [
    pygame.image.load('images/bang1.png'),
    pygame.image.load('images/bang2.png'),
    pygame.image.load('images/bang3.png'),
    ]

# Import image for bonus
image_bonuses_list = [
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
tank_coordinate_x = 100
tank_coordinate_y = 100
tank_speed = 1

# bullet start coordinate
bullets = []
bullet_coord_x = tank_coordinate_x
bullet_coord_y = tank_coordinate_y

gameplay = True

# Main loop gameplay
while gameplay:
    pygame.display.flip()
    clock.tick(60)
    screen.fill('Black')
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, 100, 600,))
    pygame.draw.rect(screen, (100, 100, 100), (700, 0, 100, 600,))
    screen.blit(bullet_image, (tank_coordinate_x + 15, tank_coordinate_y + 15))
    im = pygame.transform.rotate(image_tank_list[0], turn_1)
    screen.blit(im, (tank_coordinate_x, tank_coordinate_y))

    keys = pygame.key.get_pressed()
    #bullet movement trajectory
    if bullets:
        for bul_ind, el in enumerate(bullets):
            el.x += 12
            el.y += 12
            screen.blit(bullet_image, (el.x, el.y))

    #Tank movement controll
    if keys[pygame.K_w] and tank_coordinate_y > 0:
        tank_coordinate_y -= tank_speed
        sounds[2].play()
        turn_1 = 0
    elif keys[pygame.K_s] and tank_coordinate_y < 568:
        tank_coordinate_y += tank_speed
        sounds[2].play()
        turn_1 = 180
    elif keys[pygame.K_a] and tank_coordinate_x > 100:
        tank_coordinate_x -= tank_speed
        sounds[2].play()
        turn_1 = 90
    elif keys[pygame.K_d] and tank_coordinate_x < 668:
        tank_coordinate_x += tank_speed
        sounds[2].play()
        turn_1 = -90
    else:
        sounds[2].stop()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                bullets.append(bullet_image.get_rect(topleft=(tank_coordinate_x, tank_coordinate_y)))
                pygame.mixer.Channel(0).play(sounds[7])

        if event.type == pygame.QUIT:
            gameplay = False
pygame.quit()
