import pygame
import sys

from components.vaus import Vaus
from components.brick import Brick
from config import *
from components.settings import *
from random import randint



def handle_esc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_bt.rect.collidepoint(event.pos):
                    game_set.game_menu = False
                if level_bt.rect.collidepoint(event.pos):
                    if level_bt.level == 3:
                        level_bt.level = 1
                        level_bt.text = f"Level: {level_bt.level}"
                        level_bt.change_level = True
                    else:
                        level_bt.level += 1
                        level_bt.text = f"Level: {level_bt.level}"
                        level_bt.change_level = True


def draw_level(positions, screen):
    for i in positions:
        brick = Brick(position=i)
        brick.draw(screen)


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Arcanoid")
clock = pygame.time.Clock()

pygame.init()

vaus = Vaus()
game_set = Game_settings()
play_bt = Play()
level_bt = Level(play_bt.size[1] + 10)
rect = pygame.Rect((SCREEN_WIDGHT + 10, SCREEN_HEIGHT - 10), level_bt.size)


while True:
    handle_esc()

    if game_set.game_menu:
        screen.fill(BACKGROUND_COLOR)
        play_bt.draw(screen)
        level_bt.draw(screen)
        pygame.draw.rect(screen, level_bt.color, rect)

        if level_bt.change_level:
            level_bt.positions_for_bricks = positions_breaks(level_bt.level)
            print(level_bt.positions_for_bricks)
            level_bt.change_level = False

        clock.tick(15)
    else:
        clock.tick(35)
        screen.fill(BACKGROUND_COLOR)

        draw_level(level_bt.positions_for_bricks, screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            vaus.next_direction = "left"
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            vaus.next_direction = "right"

        vaus.update_direction()

        vaus.move()
        vaus.draw(screen)

    pygame.display.flip()