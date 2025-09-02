import pygame
import sys

def handle_keys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Arcanoid")


pygame.init()

while True:
    handle_keys()


    pygame.display.flip()