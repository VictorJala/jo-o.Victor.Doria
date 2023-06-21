import random
import pygame

from dino_runner.components.obstacles.cactus import Cactus, LargeCactus
from dino_runner.components.obstacles.Bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        self.numero_aleatorio = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if self.numero_aleatorio == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif self.numero_aleatorio == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.update_death_count()
                break

    def restart_obstacle(self):
        self.obstacles = []



    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)