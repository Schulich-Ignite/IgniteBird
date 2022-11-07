import pygame
import os

class Background(pygame.sprite.Sprite):

    def __init__(self, dimensions):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'background.png'))
        self.image = pygame.transform.scale(self.image, dimensions)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = [0,0]

