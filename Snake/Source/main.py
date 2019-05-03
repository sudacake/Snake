import sys
import pygame
import functions
from game_state import GameState
from snake import Snake
from food import Food


def main():

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(GameState.screen_size)
    pygame.display.set_caption(GameState.game_caption)
    snake = Snake()
    food = Food()

    while True:
        # frame
        pygame.time.Clock().tick(GameState.game_frames)
        # events
        functions.check_events(snake)

        # run game
        if not GameState.game_over:
            food = functions.update_food(snake, food)
            functions.update_snake(snake)

        # print
        functions.update_screen(screen)
        functions.blit_all(screen, snake, food)
        pygame.display.flip()


main()
