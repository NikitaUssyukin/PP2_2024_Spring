import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)

BACKGROUND = pygame.image.load("./resources/AnimatedStreet.png")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 35)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, 5)
        else:
            self.rect.center = (WIDTH // 2, 35)

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
E1 = Enemy()

enemies.add(E1)
all_sprites.add(P1, E1)

done = False

FPS = 60

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        print("Collision!")
        
    pygame.display.flip()
    clock.tick(FPS)