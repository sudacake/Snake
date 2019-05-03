import pygame
from box import Box
from box_state import BoxState


class Snake(pygame.sprite.Sprite):
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

    # body and forward direction
    BODY = 'snake_body'
    BODYUP = 'snake_body_up'
    BODYDOWN = 'snake_body_down'
    BODYLEFT = 'snake_body_left'
    BODYRIGHT = 'snake_body_right'

    # turn
    LEFTUP = 'snake_turn_left_up'
    UPLEFT = LEFTUP
    LEFTDOWN = 'snake_turn_left_down'
    DOWNLEFT = LEFTDOWN
    RIGHTUP = 'snake_turn_right_up'
    UPRIGHT = RIGHTUP
    RIGHTDOWN = 'snake_turn_right_down'
    DOWNRIGHT = RIGHTDOWN

    def __init__(self):
        super().__init__()
        self.own = pygame.sprite.Group()
        self.own.add(Box(BoxState(self.HEADRIGHT, self.HEADRIGHT, '', '')), 3, 0)
        self.own.add(Box(BoxState(self.BODYRIGHT, self.BODYRIGHT, self.HEADRIGHT, self.HEADRIGHT)), 2, 0)
        self.own.add(Box(BoxState(self.BODYRIGHT, self.BODYRIGHT, self.BODYRIGHT, self.BODYRIGHT)), 1, 0)
        self.own.add(Box(BoxState(self.TAILRIGHT, self.TAILRIGHT, self.BODYRIGHT, self.BODYRIGHT)), 0, 0)
    pass


