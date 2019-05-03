import sys
import pygame
from game_state import GameState
from food import Food


def check_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()

            elif event.key == pygame.K_UP:
                if snake.turn == snake.KEEP \
                        and snake.body[0].state != snake.HEADDOWN\
                        and snake.body[0].state != snake.HEADUP:
                    snake.turn = snake.UP
            elif event.key == pygame.K_DOWN:
                if snake.turn == snake.KEEP \
                        and snake.body[0].state != snake.HEADUP\
                        and snake.body[0].state != snake.HEADDOWN:
                    snake.turn = snake.DOWN
            elif event.key == pygame.K_LEFT:
                if snake.turn == snake.KEEP \
                        and snake.body[0].state != snake.HEADRIGHT\
                        and snake.body[0].state != snake.HEADLEFT:
                    snake.turn = snake.LEFT
            elif event.key == pygame.K_RIGHT:
                if snake.turn == snake.KEEP \
                        and snake.body[0].state != snake.HEADLEFT\
                        and snake.body[0].state != snake.HEADRIGHT:
                    snake.turn = snake.RIGHT


def update_screen(screen):
    screen.fill(GameState.screen_background_color)


def update_food(snake, food):
    for i in snake.body:
        if pygame.sprite.collide_rect(i, food):
            food = Food()
            snake.eat = True
            return food
    return food


def update_snake(snake):
    snake.update()
    if snake.body[0].rect.left > GameState.screen_width \
            or snake.body[0].rect.right < 0 \
            or snake.body[0].rect.top > GameState.screen_height \
            or snake.body[0].rect.bottom < 0:
        GameState.game_over = True
    for i in snake.body:
        if i != snake.body[0] and pygame.sprite.collide_rect(i, snake.body[0]):
            GameState.game_over = True


def blit_all(screen, snake, food):
    screen.blit(food.image, food.rect)
    snake.blit(screen)

