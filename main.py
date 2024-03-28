
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.update()

gameplay = True
while gameplay:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameplay = False
            pygame.quit()
