import pygame
from config import *

class Play():
    def __init__(self):
        self.position = (SCREEN_WIDGHT // 2 - PLAY_BUTTON_SIZE[0] // 2, SCREEN_HEIGHT // 2)
        self.size = PLAY_BUTTON_SIZE
        self.color = PLAY_BUTTON_COLOR
        self.text_color = PLAY_BUTTON_TEXT_COLOR
        self.text = PLAY_BUTTON_TEXT
        self.font = pygame.font.Font(None, PLAY_BUTTON_SIZE[0] // 8)
        self.rect = pygame.Rect(self.position, self.size)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class Level():
    def __init__(self, play_bt_size):
        self.level = 1
        self.position = (SCREEN_WIDGHT // 2 - LEVEL_BUTTON_SIZE[0] // 2, SCREEN_HEIGHT // 2 + play_bt_size)
        self.size = LEVEL_BUTTON_SIZE
        self.font = pygame.font.Font(None, LEVEL_BUTTON_SIZE[0] // 16)
        self.color = LEVEL_BUTTON_COLOR
        self.text_color = LEVEL_BUTTON_TEXT_COLOR
        self.text = f"Level: {self.level}"
        self.rect = pygame.Rect(self.position, self.size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)