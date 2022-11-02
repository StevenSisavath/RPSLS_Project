from ai import AI
from human import Human
from player import Player
class game:

    def __init__(self):
        self.ai = AI()
        self.human = Human()

    def display_welcome(self):
        print('''
Welcome to RPSLS!
''')

    def display_rules(self):
        print('''
Rock crushes Scissors
Scissors cuts Paper 
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
        ''')

    def choose_number_of_players(self):
        number_of_players = input('How many people are playing? 0,1 2?')
        return number_of_players

    def determine_winner(self):
        if self.choose_number_of_players() == 0:
            self.ai_1 = self.ai.choose_options()
            self.ai_2 = self.ai.choose_options()
            if self.ai_1 == 'Rock' and self.ai_2 == 'Scissors':
                print('AI 1 used rock to beat AI 2 with scissors!')

    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.choose_number_of_players()
        self.find_winner