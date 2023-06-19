import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):
    def __init__(self, image, type):
        self.type = type
        self.image = image
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH


    def update(self, game_speed, obstacle):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacle.pop()

    def draw(self, screem):
        screem.blit(self.image[self.type], (self.rect.x, self.rect.y))