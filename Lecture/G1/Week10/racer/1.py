import pygame
import os
from random import randint

pygame.init()

WIDTH = 400
HEIGHT = 600

colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

SPEED = 5

_image_library = dict()
def load_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("./resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 550)
    
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-SPEED, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(SPEED, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("./resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(self.rect.x // 2, WIDTH - self.rect.x // 2), -20)
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.y + self.rect.h >= HEIGHT:
            self.rect.center = (randint(self.rect.x // 2, WIDTH - self.rect.x // 2), -20)
        


done = False

FPS = 60
clock = pygame.time.Clock()

P1 = Player()
E1 = Enemy()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(colorWHITE)

    P1.move()
    E1.move()

    screen.blit(P1.image, P1.rect)
    screen.blit(E1.image, E1.rect)
       
    pygame.display.flip()
    clock.tick(FPS)