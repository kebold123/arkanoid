import pygame
from config import *

class Vaus():
    def __init__(self):
        self.position = (SCREEN_WIDGHT // 2 - (VAUS_SIZE[0] // 2), SCREEN_HEIGHT // 8 * 7)
        self.last_position = None
        self.size = VAUS_SIZE
        self.speed = VAUS_SPEED
        self.color = VAUS_COLOR 
        self.direction = None
        self.next_direction = None

    def update_direction(self):
        self.direction = self.next_direction
        self.next_direction = None

    def draw(self, screen):
        rect = pygame.Rect(self.position, self.size)
        pygame.draw.rect(screen, self.color, rect)

    def move(self):
        if self.direction == "left":
            if self.position[0] - self.speed <= 0:
                self.position = (0, self.position[1])
            else:
                self.position = (self.position[0] - self.speed, self.position[1])
        elif self.direction == "right":
            if self.position[0] + self.speed + self.size[0] >= SCREEN_WIDGHT:
                self.position = (SCREEN_WIDGHT - self.size[0], self.position[1])
            else:
                self.position = (self.position[0] + self.speed, self.position[1])