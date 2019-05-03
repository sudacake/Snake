import sys
import pygame
import functions
from game_state import GameState


def main():

    pygame.init()
    screen = pygame.display.set_mode((GameState.screen_width, GameState.screen_height))
    pygame.display.set_caption('Snake')

    while True:

        functions.check_events()
        functions.update_screen(screen)
        pygame.display.flip()


main()
