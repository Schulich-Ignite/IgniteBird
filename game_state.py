import enum

# the GameState class is an enum to signify the state of the game
class GameState(enum.Enum):
    START = 0
    PLAY = 1
    GAMEOVER = 2