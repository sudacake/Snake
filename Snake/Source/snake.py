import pygame
from box import Box
from game_state import GameState


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

    # forward direction
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    KEEP = ''

    def __init__(self):
        super().__init__()
        self.body = []
        self.turn = self.KEEP
        self.eat = False
        self.body.append(Box(self.HEADRIGHT, 3 * GameState.box_width, 0 * GameState.box_height))
        self.body.append(Box(self.BODY, 2 * GameState.box_width, 0 * GameState.box_height))
        self.body.append(Box(self.BODY, 1 * GameState.box_width, 0 * GameState.box_height))
        self.body.append(Box(self.TAILRIGHT, 0 * GameState.box_width, 0 * GameState.box_height))
        pass

    def update(self):

        self.update_head()
        if not self.eat:
            self.update_tail()
        self.turn = self.KEEP
        self.eat = False
        self.update_state()

    def update_head(self):
        snake_head = self.body[0]
        if self.turn != self.KEEP:
            # 1
            if self.turn == self.UP:
                if snake_head.state == self.HEADLEFT:
                    self.body.insert(1, Box(self.RIGHTUP, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.top -= GameState.box_height
                    snake_head.state = self.HEADUP
                elif snake_head.state == self.HEADRIGHT:
                    self.body.insert(1, Box(self.LEFTUP, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.top -= GameState.box_height
                    snake_head.state = self.HEADUP
                elif snake_head.state == self.HEADUP:
                    self.body.insert(1, Box(self.BODY, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.top -= GameState.box_height
                    snake_head.state = self.HEADUP
            # 2
            elif self.turn == self.DOWN:
                if snake_head.state == self.HEADLEFT:
                    self.body.insert(1, Box(self.RIGHTDOWN, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.top += GameState.box_height
                    snake_head.state = self.HEADDOWN
                elif snake_head.state == self.HEADRIGHT:
                    self.body.insert(1, Box(self.LEFTDOWN, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.top += GameState.box_height
                    snake_head.state = self.HEADDOWN
                elif snake_head.state == self.HEADDOWN:
                    self.body.insert(1, Box(self.BODY, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.top += GameState.box_height
                    snake_head.state = self.HEADDOWN

            # 3
            elif self.turn == self.LEFT:
                if snake_head.state == self.HEADUP:
                    self.body.insert(1, Box(self.LEFTDOWN, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.left -= GameState.box_width
                    snake_head.state = self.HEADLEFT
                elif snake_head.state == self.HEADDOWN:
                    self.body.insert(1, Box(self.LEFTUP, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.left -= GameState.box_width
                    snake_head.state = self.HEADLEFT
                elif snake_head.state == self.HEADLEFT:
                    self.body.insert(1, Box(self.BODY, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.top -= GameState.box_width
                    snake_head.state = self.HEADLEFT

            # 4
            elif self.turn == self.RIGHT:
                if snake_head.state == self.HEADUP:
                    self.body.insert(1, Box(self.RIGHTDOWN, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.left += GameState.box_width
                    snake_head.state = self.HEADRIGHT
                elif snake_head.state == self.HEADDOWN:
                    self.body.insert(1, Box(self.RIGHTUP, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.left += GameState.box_width
                    snake_head.state = self.HEADRIGHT
                elif snake_head.state == self.HEADLEFT:
                    self.body.insert(1, Box(self.BODY, snake_head.rect.left, snake_head.rect.top))
                    snake_head.rect.left += GameState.box_width
                    snake_head.state = self.HEADRIGHT

        else:
            self.body.insert(1, Box(self.BODY, snake_head.rect.left, snake_head.rect.top))
            if snake_head.state == self.HEADUP:
                snake_head.rect.top -= GameState.box_height
            elif snake_head.state == self.HEADDOWN:
                snake_head.rect.top += GameState.box_height
            elif snake_head.state == self.HEADLEFT:
                snake_head.rect.left -= GameState.box_width
            elif snake_head.state == self.HEADRIGHT:
                snake_head.rect.left += GameState.box_width

    def update_tail(self):
        snake_tail = self.body[len(self.body) - 1]
        snake_before_tail = self.body[len(self.body) - 2]
        snake_tail.rect = snake_before_tail.rect
        if snake_before_tail.state[:10] == self.TURN:
            if snake_before_tail.state == self.LEFTUP and snake_tail.state == self.TAILRIGHT:
                snake_tail.state = self.TAILUP
            elif snake_before_tail.state == self.LEFTUP and snake_tail.state == self.TAILDOWN:
                snake_tail.state = self.TAILLEFT
            elif snake_before_tail.state == self.RIGHTUP and snake_tail.state == self.TAILLEFT:
                snake_tail.state = self.TAILUP
            elif snake_before_tail.state == self.RIGHTUP and snake_tail.state == self.TAILDOWN:
                snake_tail.state = self.TAILRIGHT
            elif snake_before_tail.state == self.LEFTDOWN and snake_tail.state == self.TAILUP:
                snake_tail.state = self.TAILLEFT
            elif snake_before_tail.state == self.LEFTDOWN and snake_tail.state == self.TAILRIGHT:
                snake_tail.state = self.TAILDOWN
            elif snake_before_tail.state == self.RIGHTDOWN and snake_tail.state == self.TAILLEFT:
                snake_tail.state = self.TAILDOWN
            elif snake_before_tail.state == self.RIGHTDOWN and snake_tail.state == self.TAILUP:
                snake_tail.state = self.TAILRIGHT
        self.body.pop(len(self.body) - 2)

    def blit(self, screen):
        for i in self.body:
            screen.blit(i.image, i.rect)
        screen.blit(self.body[0].image, self.body[0].rect)

    def update_state(self):
        for i in self.body:
            i.image = pygame.image.load('image/' + i.state + '.png')


