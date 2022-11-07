import sys
import pygame
from pipe import Pipe

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

pipes = [
    Pipe(pygame.Rect(1500, -395, 133, 512)),
    Pipe(pygame.Rect(1500, 355, 133, 512)),
    Pipe(pygame.Rect(2100, -257, 133, 512)),
    Pipe(pygame.Rect(2100, 493, 133, 512)),

]


while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()

    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_SPACE]:
        pass
    if keys_pressed[pygame.K_p]:
        pass
    if keys_pressed[pygame.K_RIGHT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_DOWN]:
        pass  # Replace this line

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the
    # (x, y) coordinate

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        pass  # Replace this line
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line

    """
    UPDATE section - manipulate everything on the screen
    """
    
    for pipe in pipes:
        pipe.update()
        
    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour
    for pipe in pipes:
        pygame.draw.rect(screen, (255, 0, 0), pipe.rect)
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second

