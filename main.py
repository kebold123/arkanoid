import pygame
import sys

from components.vaus import Vaus
from components.brick import Brick
from components.ball import Ball
from config import *
from components.settings import *
from random import randint

def create_screen():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Arcanoid")
    clock = pygame.time.Clock()
    return screen, clock

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
    bricks = []
    for i in positions:
        brick = Brick(position=i)
        bricks.append(brick)
        brick.draw(screen)
    return bricks

def game_menu(screen):
    screen.fill(BACKGROUND_COLOR)
    play_bt.draw(screen)
    level_bt.draw(screen)

def create_variables():
    vaus = Vaus()
    game_set = Game_settings()
    play_bt = Play()
    level_bt = Level(play_bt.size[1] + 10)
    ball = Ball()
    return vaus, game_set, play_bt, level_bt, ball

def ball_action(ball, vaus, bricks, screen):
    if ball.in_game:
        ball.move()
        ball.check_collision(vaus, bricks)
        ball.draw(screen)

def vaus_move(keys, vaus):
    if keys[pygame.K_LEFT]:
        vaus.next_direction = "left"
    elif keys[pygame.K_RIGHT]:
        vaus.next_direction = "right"

def vaus_actions(screen, vaus):
    vaus.update_direction()
    vaus.move()
    vaus.draw(screen)

def change_level(level_bt):
    if level_bt.change_level:
        level_bt.positions_for_bricks = positions_breaks(level_bt.level)
        level_bt.change_level = False

pygame.font.init()
pygame.init()

vaus, game_set, play_bt, level_bt, ball = create_variables()
screen, clock = create_screen()



while True:
    handle_esc()

    if game_set.game_menu:

        game_menu(screen)
        change_level(level_bt)

        clock.tick(15)
    else:
        clock.tick(35)
        screen.fill(BACKGROUND_COLOR)

        bricks = draw_level(level_bt.positions_for_bricks, screen)
        ball_action(ball, vaus, bricks, screen)

        vaus_move(pygame.key.get_pressed(), vaus)
        vaus_actions(screen, vaus)

    pygame.display.flip()