import pygame
import sys

from vaus import Vaus
from config import *

def handle_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Arcanoid")
clock = pygame.time.Clock()

pygame.init()

vaus = Vaus()

while True:
    clock.tick(10)
    screen.fill(BACKGROUND_COLOR)

    handle_keys()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        vaus.next_direction = "left"
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        vaus.next_direction = "right"

    vaus.update_direction()

    vaus.move()
    vaus.draw(screen)

    pygame.display.flip()