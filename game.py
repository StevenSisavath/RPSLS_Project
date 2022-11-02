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
            print(f'ai1 {self.ai_1} ')
            self.ai_2 = self.ai.choose_options()
            print(f'ai2 has {self.ai_2} ')
            if self.ai_1 == 'Rock' and self.ai_2 == 'Scissors' or 'Lizard':
                print('AI 1 beat AI_2')
            elif self.ai_1 == 'Paper' and self.ai_2 == 'Rock' or 'Spock':
                print('AI 1 beat AI_2')
            elif self.ai_1 == 'Scissors' and self.ai_2 == 'Paper' or 'Lizard':
                print('AI 1 beat AI_2')
            elif self.ai_1 == 'Lizard' and self.ai_2 == 'Spock' or 'Paper':
                print('AI 1 beat AI_2')
            elif self.ai_1 == 'Spock' and self.ai_2 == 'Scissors' or 'Rock':
                print('AI 1 beat AI_2')

            elif self.ai_2 == 'Rock' and self.ai_1 == 'Scissors' or 'Lizard':
                print('AI 2 beat AI_1')
            elif self.ai_2 == 'Paper' and self.ai_1 == 'Rock' or 'Spock':
                print('AI 2 beat AI_1')
            elif self.ai_2 == 'Scissors' and self.ai_1 == 'Paper' or 'Lizard':
                print('AI 2 beat AI_1')
            elif self.ai_2 == 'Lizard' and self.ai_1 == 'Spock' or 'Paper':
                print('AI 2 beat AI_1')
            elif self.ai_2 == 'Spock' and self.ai_1 == 'Scissors' or 'Rock':
                print('AI 2 beat AI_1')


    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.choose_number_of_players()
        self.find_winner