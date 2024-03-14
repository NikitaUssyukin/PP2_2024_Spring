import pygame

print(list(filter(lambda x: 'K_' in x, dir(pygame))))

print(pygame.K_SPACE)

pygame.init()

keys = pygame.key.get_pressed()

print(keys)

print(keys[pygame.K_SPACE])

