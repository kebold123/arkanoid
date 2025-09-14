import pygame
import math

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
        self.in_game = check_ingame(self.position)
        self.m = self.size * 2 
        self.x_v = 5
        self.y_v = 5
    
    def draw(self, screen):
        if self.in_game:
            pygame.draw.circle(screen, self.color, self.position, self.size)

    def move(self):
        if self.in_game:
            self.position = (self.position[0] + self.x_v, self.position[1] - self.y_v)

    def check_collision(self, vaus, bricks):
        pass
        