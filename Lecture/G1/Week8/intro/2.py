import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

done = False

x = 30
y = 60

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y += 10
            if event.key == pygame.K_UP:
                y -= 10
            if event.key == pygame.K_RIGHT:
                x += 10
            if event.key == pygame.K_LEFT:
                x -= 10

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 200, 100))
    pygame.display.flip()
        
    
        

        