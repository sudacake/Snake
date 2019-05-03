import pygame
import random
from game_state import GameState


class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('image/food.png')
        self.x = random.randrange(0, 50) * GameState.food_height
        self.y = random.randrange(0, 50) * GameState.food_width
        self.rect = pygame.rect.Rect(self.x, self.y,
                                     GameState.food_width, GameState.food_height)

    def update(self):
        pass
