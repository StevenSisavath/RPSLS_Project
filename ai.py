from player import Player
import random
class AI(Player):

    def __init__(self):
        super().__init__()

    def choose_options(self):
        return random.choice(self.options)