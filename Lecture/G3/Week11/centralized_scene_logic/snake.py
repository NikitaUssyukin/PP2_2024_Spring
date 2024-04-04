import pygame
from color_palette import *

def draw_grid(screen, width, height, cell):
    for i in range(height // 2):
        for j in range(width // 2):
            pygame.draw.rect(screen, colorGRAY, (i * cell, j * cell, cell, cell), 1)

def draw_grid_chess(screen, width, height, cell):
    colors = [colorWHITE, colorGRAY]

    for i in range(height // 2):
        for j in range(width // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * cell, j * cell, cell, cell))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0

    # def move(self):
    #     head = self.body[0]
    #     self.body.pop()

    #     new_x = head.x + self.dx
    #     new_y = head.y + self.dy

    #     new_head = Point(new_x, new_y)
    #     self.body.insert(0, new_head)

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

    def draw(self, screen, cell):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * cell, head.y * cell, cell, cell))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * cell, segment.y * cell, cell, cell))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            return True

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self, screen, cell):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * cell, self.pos.y * cell, cell, cell))