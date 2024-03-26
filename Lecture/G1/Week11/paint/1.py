import pygame

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))

done = False

prevX = -1
prevY = -1
currX = -1
currY = -1

LMBPressed = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB was clicked!")
            print(event.pos)
            LMBPressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBPressed:
                currX = event.pos[0]
                currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB was released!")
            print(event.pos)
            LMBPressed = False
            currX = event.pos[0]
            currY = event.pos[1]

    if LMBPressed:
        screen.fill((0, 0, 0))
        
    if LMBPressed:
        pygame.draw.rect(screen, (255, 0, 0), (prevX, prevY, currX - prevX, currY - prevY), 2)

    pygame.display.flip()