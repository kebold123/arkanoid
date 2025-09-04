import pygame
from config import *

class Vaus():
    def __init__(self):
        self.position = (SCREEN_WIDGHT // 2 - 10, CENTER[1])
        self.last_position = None
        self.size = (20, 10)
        self.speed = 10
        self.color = (255, 255, 255) 
        self.direction = None

    def draw(self, screen):
        rect = pygame.Rect(self.position, self.size)
        pygame.draw.rect(screen, self.color, rect)

    def move(self, direction=None):
        if direction == None:
            pass
        elif direction == "left":
            self.position = (self.position[0] - self.speed, self.position[1])
        elif direction == "right":
            self.position = (self.position[0] + self.speed, self.position[1])