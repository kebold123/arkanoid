import pygame
from config import *

class Brick():
    def __init__(self):
        self.size = BRICK_SIZE
        self.color = BRICK_COLOR
        self.position = None
        self.hitbox = None
        self.is_destroyed = False
    
    def draw(self, screen):
        pass