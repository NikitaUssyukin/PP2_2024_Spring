import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

image = pygame.image.load('ball.png')

done = False

x = 30
y = 60

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            y += 3
        if event.key == pygame.K_UP:
            y -= 3
        if event.key == pygame.K_RIGHT:
            x += 3    
        if event.key == pygame.K_LEFT:
            x -= 3

    screen.fill((255, 255, 255))
    
    screen.blit(image, (x, y))

    pygame.display.flip()
    clock.tick(60)
        
    
        

        