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

    # body and forward direction
    BODY = 'snake_body'
    BODYUP = 'snake_body_up'
    BODYDOWN = 'snake_body_down'
    BODYLEFT = 'snake_body_left'
    BODYRIGHT = 'snake_body_right'

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
        self.image = pygame.image.load('image/' + state.now + '.png')
        self.rect = pygame.rect.Rect(left, top, self.GameState.box_width, self.GameState.box_height)
        self.state = state
        pass

    def update(self):
        if self.state.now[:10] == self.HEAD:
            self.update_head()
        elif self.state.now[:10] == self.TAIL:
            self.update_tail()
        elif self.state.now[:10] == self.BODY:
            self.update_body()
        elif self.state.now[:10] == self.TURN:
            self.update_turn()

        self.update_state()

        pass

    def update_head(self):
        if self.state.now == self.HEADUP:
            self.rect.top -= GameState.box_height
        elif self.state.now == self.HEADDOWN:
            self.rect.top += GameState.box_height
        elif self.state.now == self.HEADLEFT:
            self.rect.left -= GameState.box_width
        elif self.state.now == self.HEADRIGHT:
            self.rect.left += GameState.box_width

    def update_tail(self):
        # 1
        if self.state.now == self.TAILUP:
            self.rect.top -= GameState.box_height
            if self.state.pre_now[:10] != self.TURN:
                pass
            elif self.state.pre_now == self.DOWNLEFT:
                self.state.now = self.TAILLEFT
            elif self.state.pre_now == self.DOWNRIGHT:
                self.state.now = self.TAILRIGHT
        # 2
        elif self.state.now == self.TAILDOWN:
            self.rect.top += GameState.box_height
            if self.state.pre_now[:10] != self.TURN:
                pass
            elif self.state.pre_now == self.UPLEFT:
                self.state.now = self.TAILLEFT
            elif self.state.pre_now == self.UPRIGHT:
                self.state.now = self.TAILRIGHT
        # 3
        elif self.state.now == self.TAILLEFT:
            self.rect.left -= GameState.box_width
            if self.state.pre_now[:10] != self.TURN:
                pass
            elif self.state.pre_now == self.RIGHTUP:
                self.state.now = self.TAILUP
            elif self.state.pre_now == self.RIGHTDOWN:
                self.state.now = self.TAILDOWN
        # 4
        elif self.state.now == self.TAILRIGHT:
            self.rect.left += GameState.box_width
            if self.state.pre_now[:10] != self.TURN:
                pass
            elif self.state.pre_now == self.LEFTUP:
                self.state.now = self.TAILUP
            elif self.state.pre_now == self.LEFTDOWN:
                self.state.now = self.TAILDOWN

    def update_body(self):
        # 1
        if self.state.now == self.BODYUP:
            self.rect.top -= GameState.box_height
            if self.state.pre_now[:10] != self.TURN:
                pass
            elif self.state.pre_now == self.DOWNLEFT:
                self.state.now = self.DOWNLEFT
            elif self.state.pre_now == self.DOWNRIGHT:
                self.state.now = self.DOWNRIGHT

        # 2
        elif self.state.now == self.BODYDOWN:
            self.rect.top += GameState.box_height
            if self.state.pre_now[:10] != self.TURN:
                pass
            elif self.state.pre_now == self.UPLEFT:
                self.state.now = self.UPLEFT
            elif self.state.pre_now == self.UPRIGHT:
                self.state.now = self.UPRIGHT

        # 3
        elif self.state.now == self.BODYLEFT:
            self.rect.left -= GameState.box_width
            if self.state.pre_now[:10] != self.TURN:
                pass
            elif self.state.pre_now == self.RIGHTUP:
                self.state.now = self.RIGHTUP
            elif self.state.pre_now == self.RIGHTDOWN:
                self.state.now = self.RIGHTDOWN

        # 4
        elif self.state.now == self.BODYRIGHT:
            self.rect.left += GameState.box_width
            if self.state.pre_now[:10] != self.TURN:
                pass
            elif self.state.pre_now == self.LEFTUP:
                self.state.now = self.LEFTUP
            elif self.state.pre_now == self.LEFTDOWN:
                self.state.now = self.LEFTDOWN

    def update_turn(self):
        pass



