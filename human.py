from player import Player
class Human(Player):

    def __init__(self):
        super().__init__()

    def choose_options(self):
        return str(input('What would you like to choose? Rock/Paper/Scissors/Lizard/Spock?')) #for the sake of the question, input should be exactly what options there are.