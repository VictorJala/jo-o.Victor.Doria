import pygame
import random

from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import *


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.death_sound = DEATH_SOUND
        self.score = 0

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
        ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up and game.vida == 1:
                    self.death_sound.play()  
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break
                
                elif game.player.type == HAMMER_TYPE:
                    self.obstacles.remove(obstacle)
        
                elif game.player.type == DEFAULT_TYPE:
                    self.obstacles.remove(obstacle)
                    game.vida -= 1


    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)