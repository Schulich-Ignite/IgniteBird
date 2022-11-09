import pygame
import os

# The class for the player. Inherits from sprite
class Bird(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', 'bird.png')).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.center = position

        self.speed_y = 0
        self.gravity = 0.6

    # updates every game loop, applies gravity to bird every frame
    def update(self):
        self.move()
        self.speed_y += self.gravity
    
    # updates the birds y speed to make them move
    def move(self):
        self.rect.y += self.speed_y

    # changes the birds y speed to negative to make them move upwards
    def jump(self):
        self.speed_y = -10

