from ai import AI
from human import Human
from player import Player
class Game:

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
        return int(input('How many players are there?'))

    def determine_winner(self):
        self.number_of_players = self.choose_number_of_players()
        print('')
        if self.number_of_players == 0:
            self.ai_1 = self.ai.choose_options()
            print(f'AI 1 has {self.ai_1}!')
            self.ai_2 = self.ai.choose_options()
            print(f'AI 2 has {self.ai_2}!')
   
        elif self.number_of_players == 1:
            self.ai_1 = self.ai.choose_options()
            print(f'AI 1 has {self.ai_1}!')
            self.human_1 = self.human.choose_options()
            print(f'Player 1 has {self.human_1}!')

        elif self.number_of_players == 2:
            self.human_1 = self.human.choose_options()
            print(f'Player 1 has {self.human_1}!')
            self.human_2 = self.human.choose_options()
            print(f'Player 2 has {self.human_2}!')
            if self.human_1 == 'Rock':
                if self.human_2 == 'Scissors' or self.human_2 == 'Lizard':
                    print('Player 1 beat the Player 2!')
                elif self.human_2 == 'Paper' or self.human_2 == 'Spock':
                    print('Player 2 beat the Player 1!')
                elif self.human_2 == 'Rock':
                    print('Player 1 tied Player 2!')
            elif self.human_1 == 'Scissors':
                if self.human_2 == 'Paper' or self.human_2 == 'Lizard':
                    print('Player 1 beat the Player 2!')
                elif self.human_2 == 'Rock' or self.human_2 == 'Spock':
                    print('Player 2 beat the Player 1!')
                elif self.human_2 == 'Scissors':
                    print('Player 1 tied Player 2!')


    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.determine_winner()