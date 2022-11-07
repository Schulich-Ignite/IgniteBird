import pygame
import os

class Bird(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'bird.png')).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.center = position

        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 0.6

    def update(self):
        self.move(self.speed_x, self.speed_y)
        self.speed_y += self.gravity
 
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
 
    def jump(self):
        self.speed_y = -10

