import pygame
import pygame.freetype
import os

def create_text(text, font_size, text_color):
    font = pygame.freetype.Font(os.path.join("assets", "joystixmonospace.ttf"), font_size)
    surface, _ = font.render(text=text, fgcolor=text_color)
    return surface.convert_alpha()

class UIElement(pygame.sprite.Sprite):

    def __init__(self, text, position, font_size, color, font_color=(255,255,255)):
        super().__init__()
        self.padding = 50
        self.image = create_text(text, font_size, font_color)
        self.font_size = font_size
        self.font_color = font_color

        self.rect = self.image.get_rect(center=(position[0] - self.padding / 2, position[1] - self.padding /2))

        self.border = self.rect.copy()
        self.border.center = (position[0] - 2 - self.padding / 2, position[1] - 2 - self.padding /2) 
        self.border.width = self.border.width + 4 + self.padding
        self.border.height = self.border.height + 4 + self.padding

        self.rect.width = self.rect.width + self.padding
        self.rect.height = self.rect.height + self.padding

        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.border)
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.image, (self.rect.x + self.padding / 2, self.rect.y + self.padding / 2))

