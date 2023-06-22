import random
import pygame

from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.life_extra import Heart
#from dino_runner.components.power_ups.mais_score import Mais_score
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.utils.constants import *


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, score):
        self.aleatorio_number = random.randint(0, 2)
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            if self.aleatorio_number == 0:
                self.power_ups.append(Hammer())
            elif self.aleatorio_number == 1:
                self.power_ups.append(Shield())
            elif self.aleatorio_number == 2:
                 self.power_ups.append(Heart())
            #elif self.aleatorio_number == 3:
               # self.power_ups.append(Mais_score())


    def update(self, game):
        self.generate_power_up(game.score)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up.rect):
                if game.player.type == DEFAULT_TYPE and isinstance(power_up, Heart):
                    COIN_SOUND.play()
                    game.vida += 1
                    game.player.has_power_up = False
                    self.power_ups.remove(power_up)
                    
                # elif game.player.type == DEFAULT_TYPE and isinstance(power_up, Mais_score):
                #     game.maisScore()
                #     game.screen.fill((0,0,0))
                #     game.player.has_power_up = False
                #     draw_message_component('200 points added to score',
                #                                 game.screen,
                #                                 pos_x_center= 300,
                #                                 pos_y_center = 500)
                #     self.power_ups.remove(power_up) 
            
                else:
                    COIN_SOUND.play()
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.type = power_up.type
                    game.player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)