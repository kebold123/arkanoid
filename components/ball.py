import pygame
from config import *


def check_ingame(position):
        if position[1] > SCREEN_HEIGHT + 10:
            return False
        else:
            return True
        

class Ball():
    def __init__(self):
        self.position = CENTER[0], CENTER[1] + 100
        self.size = BALL_SIZE
        self.color = BALL_COLOR
        self.speed = 5
        self.in_game = check_ingame(self.position)
    
    def draw(self, screen):
        if self.in_game:
            pygame.draw.circle(screen, self.color, self.position, self.size)