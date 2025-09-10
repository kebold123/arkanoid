import pygame
from config import *

class Brick():
    def __init__(self, position, color=BRICK_COLOR):
        self.size = BRICK_SIZE
        self.color = color
        self.position = position
        self.is_destroyed = False
        self.rect = pygame.Rect(self.position, self.size)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)