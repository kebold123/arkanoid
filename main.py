import pygame
import sys

from components.vaus import Vaus
from components.brick import Brick
from components.ball import Ball
from config import *
from components.settings import *
from random import randint

def create_screen():
    screen = pygame.display.set_mode((SCREEN_WIDGHT, SCREEN_HEIGHT))
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

def game_menu(screen):
    screen.fill(BACKGROUND_COLOR)
    play_bt.draw(screen)
    level_bt.draw(screen)

def create_variables(screen):
    vaus = Vaus()
    game_set = Game_settings()
    play_bt = Play()
    level_bt = Level(play_bt.size[1] + 10, screen)
    ball = Ball()
    return vaus, game_set, play_bt, level_bt, ball

def ball_action(ball, vaus, bricks, screen):
    if ball.in_game:
        ball.move()
        ball.check_collision(ball, vaus, bricks)
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
        level_bt.bricks = create_breaks(level_bt.level)
        level_bt.change_level = False

def draw_bricks(screen, bricks):
    for i in range(len(bricks)):
        bricks[i].draw(screen)
     

pygame.font.init()
pygame.init()

screen, clock = create_screen()
vaus, game_set, play_bt, level_bt, ball = create_variables(screen)



while True:
    handle_esc()

    if game_set.game_menu:

        game_menu(screen)

        clock.tick(15)
    else:
        clock.tick(35)
        screen.fill(BACKGROUND_COLOR)

        draw_bricks(screen, level_bt.bricks)
        ball_action(ball, vaus, level_bt.bricks, screen)

        vaus_move(pygame.key.get_pressed(), vaus)
        vaus_actions(screen, vaus)

    pygame.display.flip()