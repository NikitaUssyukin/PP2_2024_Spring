import pygame
import os
from random import randint
from time import sleep
import sys

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

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

_image_library = dict()
def load_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

BACKGROUND = load_image("./resources/AnimatedStreet.png")

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
        self.rect.center = (randint(self.rect.w // 2, WIDTH - self.rect.w // 2), -20)
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.y + self.rect.h >= HEIGHT:
            self.rect.center = (randint(self.rect.w // 2, WIDTH - self.rect.w // 2), -20)
        


done = False

FPS = 60
clock = pygame.time.Clock()

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

enemies.add(E1)
all_sprites.add(E1, P1)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            SPEED += 1

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill(colorRED)
        pygame.display.flip()
        sleep(2)
        pygame.quit()
        sys.exit()
       
    pygame.display.flip()
    clock.tick(FPS)