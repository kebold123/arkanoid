import pygame
import sys

from components.vaus import Vaus
from config import *
from components.settings import *

def handle_esc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def button_clicked():
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Arcanoid")
clock = pygame.time.Clock()

pygame.init()

vaus = Vaus()
game_set = Game_settings()
play_bt = Play()
level_bt = Level(play_bt.size[1] + 10)

while True:
    handle_esc()

    if game_set.game_menu:
        play_bt.draw(screen)
        level_bt.draw(screen)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            if play_bt.rect.collidepoint(mouse_pos):
                game_set.game_menu = False
            if level_bt.rect.collidepoint(mouse_pos):
                if level_bt.level == 3:
                    level_bt.level = 1
                    level_bt.text = f"Level: {level_bt.level}"
                else:
                    level_bt.level += 1
                    level_bt.text = f"Level: {level_bt.level}"

        clock.tick(10)
    else:
        clock.tick(10)
        screen.fill(BACKGROUND_COLOR)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            vaus.next_direction = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vaus.next_direction = "right"

        vaus.update_direction()

        vaus.move()
        vaus.draw(screen)

    pygame.display.flip()