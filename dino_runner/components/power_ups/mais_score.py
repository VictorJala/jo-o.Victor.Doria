from dino_runner.utils.constants import MAIS_SCORE, DEFAULT_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Mais_score(PowerUp):
    def __init__(self):
        self.image = MAIS_SCORE
        self.type = DEFAULT_TYPE
        super().__init__(self.image, self.type)