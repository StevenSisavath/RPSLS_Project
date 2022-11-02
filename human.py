from player import Player
class Human(Player):

    def __init__(self):
        super().__init__()

    def choose_options(self):
        return input('What would you like to choose?')