import sys
import os
import pygame
from ui_element import UIElement
from bird import Bird
from pipe import PipeGroup
from game_state import GameState

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ORANGE = (255, 165, 0)
LIGHT_ORANGE = (255, 192, 72)

# Useful functions

# This function determines if the bird has reached a gameover state (moved off screen or hit pipe)
def gameOver(bird, pipeGroup):
    if(bird.rect.y >= SCREEN_HEIGHT or bird.rect.y <= 0):
        return True
    if(pipeGroup.collide(bird)):
        return True
    return False

# This function returns 1 if the bird has passed an eligible pipe or returns 0 if the bird hasn't
def pointReceived(bird, pipeGroup):
    if(pipeGroup.passed):
        return 0
    if(bird.rect.centerx <= pipeGroup.top_pipe.rect.centerx):
        return 0
    pipeGroup.setPassed()
    return 1

# Function to help create score UI elements
def createScoreElement(text, x=SCREEN_WIDTH/2):
    return UIElement(text= text,
    font_size= 30,
    position = (x, SCREEN_HEIGHT/12),
    color=ORANGE)



# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Inserting background in SETUP
background = pygame.image.load(os.path.join("assets", "background.png")).convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_WIDTH))
screen_rect = screen.get_rect()

# Initializing the UI elements
score_element = createScoreElement(str(0))
high_score_element = createScoreElement(str(0))

title = UIElement(
    text="IGNITE BIRD", 
    font_size=100, 
    position=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4),
    color=ORANGE
    )

start_text = UIElement(
    text="PRESS SPACE TO PLAY", 
    font_size=40, 
    position=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150),
    color=ORANGE
)

game_over_text = UIElement(
    text="GAME OVER",
    font_size=40,
    position=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 20),
    color=ORANGE
)

restart_text = UIElement(
    text="PRESS P TO TRY AGAIN",
    font_size=40,
    position=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 80),
    color=ORANGE
)

# Setting initial state of the game
game_state = GameState.START
players = pygame.sprite.Group()
bird = Bird((SCREEN_WIDTH /2 , SCREEN_HEIGHT/2))
players.add(bird)

pipes = pygame.sprite.Group()

pipeGroups = [
    PipeGroup(SCREEN_WIDTH + 500),
    PipeGroup(SCREEN_WIDTH + 1100)
]

pipes.add(pipeGroups[0].bot_pipe)
pipes.add(pipeGroups[0].top_pipe)

pipes.add(pipeGroups[1].bot_pipe)
pipes.add(pipeGroups[1].top_pipe)

score = 0
high_score = 0

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
        if game_state == GameState.START:
            game_state = GameState.PLAY
        elif game_state == GameState.PLAY:
            bird.jump()
    if keys_pressed[pygame.K_p]:
        if game_state == GameState.GAMEOVER:
            players = pygame.sprite.Group()
            bird = Bird((SCREEN_WIDTH /2 , SCREEN_HEIGHT/2))
            players.add(bird)

            pipes = pygame.sprite.Group()

            pipeGroups = [
                PipeGroup(SCREEN_WIDTH + 500),
                PipeGroup(SCREEN_WIDTH + 1100)
            ]

            pipes.add(pipeGroups[0].bot_pipe)
            pipes.add(pipeGroups[0].top_pipe)

            pipes.add(pipeGroups[1].bot_pipe)
            pipes.add(pipeGroups[1].top_pipe)

            game_state = GameState.START

            score = 0
            score_element = createScoreElement(str(0))

            high_score_element = createScoreElement("BEST: " + str(high_score), SCREEN_WIDTH/6)
        
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
    
    # Only need to update while the game is in the play state
    if game_state == GameState.PLAY:
        for group in pipeGroups:
            group.update()
            #check if the bird has receive a point from the pipe group
            point = pointReceived(bird, group)

            #check if the game has reached a gameover state, set to play if not
            game_state = GameState.GAMEOVER if game_state == GameState.GAMEOVER or gameOver(bird, group) else GameState.PLAY

            #check if a point has received a point then create a new score element with updated point
            if(point == 1):
                score += point
                score_element = createScoreElement(str(score))
            
            #check if the game_state is gameover then create high score element if the current score was higher
            if game_state == GameState.GAMEOVER:
                high_score = score if score > high_score else high_score
                high_score_element = createScoreElement("BEST: " + str(high_score), SCREEN_WIDTH/6)
    
        players.update()
        
    """
    DRAW section - make everything show up on screen
    """
    # Draw background in DRAW
    screen.blit(background, screen_rect)

    # Draw the title screen if the game is in the start state
    if game_state == GameState.START:
        title.draw(screen)
        start_text.draw(screen)
    
    # Draw the player always as it appears in the start, gameover and play state
    players.draw(screen)

    # Draw the pipes and score if the game isn't in the start state
    if not game_state == GameState.START:
        pipes.draw(screen)
        score_element.draw(screen)

    # Draw the high score state if the high score state has been set and is greater than 0
    if high_score > 0:
        high_score_element.draw(screen)

    # Draw the the gameover screen if the state is gameover
    if game_state == GameState.GAMEOVER:
        game_over_text.draw(screen)
        restart_text.draw(screen)

    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second

