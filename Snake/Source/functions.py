import sys
import pygame
from game_state import GameState


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen):
    screen.fill(GameState.screen_background_color)
