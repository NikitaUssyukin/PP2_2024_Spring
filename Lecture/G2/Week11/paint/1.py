import pygame
import sys

pygame.init()

WIDTH = 960
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

done = False

LMBpressed = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            if LMBpressed:
                pygame.draw.rect(screen, (255, 255, 0), (event.pos[0], event.pos[1], 1, 1))
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            LMBpressed = False

    pygame.display.flip()