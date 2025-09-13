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
        self.speed = 5
        self.v = self.speed
        self.t = self.speed // 60
        self.m = self.size * 2
        self.cos = math.cos(math.radians(45))
        self.sin = math.sin(math.radians(45))
    
    def draw(self, screen):
        if self.in_game:
            pygame.draw.circle(screen, self.color, self.position, self.size)

    def move(self):
        if self.in_game:
            self.position = (self.position[0] + self.v * self.cos, self.position[1] - self.v * self.sin)
        else:
            self.position = (self.position[0], self.position[1] + self.speed)
            self.in_game = check_ingame(self.position)