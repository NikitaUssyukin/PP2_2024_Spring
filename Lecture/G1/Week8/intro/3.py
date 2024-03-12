import pygame

print(list(filter(lambda x: 'K_' in x, dir(pygame))))

print(pygame.K_SPACE)

pygame.init()

pressed = pygame.key.get_pressed()

print(pressed[pygame.K_SPACE])

