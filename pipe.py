import pygame
import os
import random

class Pipe(pygame.sprite.Sprite):

    def __init__(self, x, y, flipped):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "pipe.png"))
        self.image = pygame.transform.flip(self.image, flip_x = False, flip_y = flipped)
        self.rect = self.image.get_rect()

        self.bottom = flipped
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.x -= self.speed
        if(self.rect.x < -self.rect.width):
            self.rect.x = 1000
            return True
        return False

class PipeGroup():

    def __init__(self, x): 

        top_y, bot_y = self.random_y()
        self.top_pipe = Pipe(x, top_y, True)
        self.bot_pipe = Pipe(x, bot_y, False)
        self.passed = False

    def random_y(self):
        bot_offset = 750
        min_y = -400
        max_y = -40

        top_height = random.randint(min_y, max_y)
        bot_height = top_height + bot_offset

        return (top_height, bot_height)

    def setPassed(self):
        self.passed = True

    def update(self):
        crossed = self.top_pipe.update()
        self.bot_pipe.update()

        if(crossed):
            self.passed = False
            top_y, bot_y = self.random_y()
            self.top_pipe.rect.y = top_y
            self.bot_pipe.rect.y = bot_y
    
    def collide(self, bird):
        return bird.rect.colliderect(self.top_pipe.rect) or bird.rect.colliderect(self.bot_pipe.rect)

