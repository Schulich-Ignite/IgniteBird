import pygame
import os

class Bird(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'bird.png')).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.center = position

        self.speed_y = 0
        self.gravity = 0.6

    def update(self):
        self.move(self.speed_y)
        self.speed_y += self.gravity
 
    def move(self, y):
        self.rect.y += y
 
    def jump(self):
        self.speed_y = -10

