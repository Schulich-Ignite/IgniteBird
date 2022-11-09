import pygame
import os
import random

# The Pipe class is the main obstacle in the game. Can be rendered rightside up or upside down
class Pipe(pygame.sprite.Sprite):

    # creates a pipe at the specified x and y as well as if it needs to be rendered flipped or not
    def __init__(self, x, y, flipped):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "pipe.png"))
        self.image = pygame.transform.flip(self.image, flip_x = False, flip_y = flipped)
        self.rect = self.image.get_rect()

        self.bottom = flipped
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    # update the pipes position, returns true if the pipe goes off the right side of the screen and false if not
    def update(self):
        self.rect.x -= self.speed
        if(self.rect.x < -self.rect.width):
            self.rect.x = 1000
            return True
        return False

# The PipeGroup class holds a bottom and a top pipe which the player wants to fly through
class PipeGroup:

    # creates a group of pipes (top and bottom) based on an x position
    def __init__(self, x): 

        top_y, bot_y = self.random_y()
        self.top_pipe = Pipe(x, top_y, True)
        self.bot_pipe = Pipe(x, bot_y, False)

        # This tells the game when a pipe has been passed which helps accuratly calculate points
        self.passed = False

    # creates two random y values for the top and bottom pipe respectively. 
    # This function guarantees a consistent distance between pipes and that the gap is on the screen.
    def random_y(self):
        bot_offset = 750
        min_y = -400
        max_y = -40

        top_height = random.randint(min_y, max_y)
        bot_height = top_height + bot_offset

        return (top_height, bot_height)

    # sets the passed value to true. Used when the player has passed a PipeGroup
    def setPassed(self):
        self.passed = True

    # updates the pieps in the pipe group and reinitializes the pipes on the left side of the screen 
    # if they crossed the right side.
    def update(self):
        crossed = self.top_pipe.update()
        self.bot_pipe.update()

        if(crossed):
            self.passed = False
            top_y, bot_y = self.random_y()
            self.top_pipe.rect.y = top_y
            self.bot_pipe.rect.y = bot_y
    
    # Determines if the bird has collided with the bottom or top pipe in the group
    def collide(self, bird):
        return bird.rect.colliderect(self.top_pipe.rect) or bird.rect.colliderect(self.bot_pipe.rect)

