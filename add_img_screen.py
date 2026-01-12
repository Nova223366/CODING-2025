import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500  # Key word likly

display_surface = pygame.display.set_mod((SCREEN_WIDTH, SCREEN_HEIGHT))

background = image = pygame.transform.scale