import pygame
from game_state import GameState


class Box(pygame.sprite.Sprite):
    # head and forward direction
    HEAD = 'snake_head'
    HEADUP = 'snake_head_up'
    HEADDOWN = 'snake_head_down'
    HEADLEFT = 'snake_head_left'
    HEADRIGHT = 'snake_head_right'

    # tail and forward direction
    TAIL = 'snake_tail'
    TAILUP = 'snake_tail_up'
    TAILDOWN = 'snake_tail_down'
    TAILLEFT = 'snake_tail_left'
    TAILRIGHT = 'snake_tail_right'

    # body
    BODY = 'snake_body'

    # turn
    TURN = 'snake_turn'
    LEFTUP = 'snake_turn_left_up'
    UPLEFT = LEFTUP
    LEFTDOWN = 'snake_turn_left_down'
    DOWNLEFT = LEFTDOWN
    RIGHTUP = 'snake_turn_right_up'
    UPRIGHT = RIGHTUP
    RIGHTDOWN = 'snake_turn_right_down'
    DOWNRIGHT = RIGHTDOWN

    def __init__(self, state, left, top):
        super().__init__()
        self.image = pygame.image.load('image/' + state + '.png')
        self.rect = pygame.rect.Rect(left, top, GameState.box_width, GameState.box_height)
        self.state = state
        pass

    def update(self):
        pass


