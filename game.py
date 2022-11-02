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
            print(f'AI 1 has {self.ai_1}!')
            self.ai_2 = self.ai.choose_options()
            print(f'AI 2 has {self.ai_2}!')
            if self.ai_1 == 'Rock' and self.ai_2 == 'Scissors' or 'Lizard':
                print('AI 1 beat AI 2!')
            elif self.ai_1 == 'Paper' and self.ai_2 == 'Rock' or 'Spock':
                print('AI 1 beat AI 2!')
            elif self.ai_1 == 'Scissors' and self.ai_2 == 'Paper' or 'Lizard':
                print('AI 1 beat AI 2!')
            elif self.ai_1 == 'Lizard' and self.ai_2 == 'Spock' or 'Paper':
                print('AI 1 beat AI 2!')
            elif self.ai_1 == 'Spock' and self.ai_2 == 'Scissors' or 'Rock':
                print('AI 1 beat AI 2!')
            elif self.ai_2 == 'Rock' and self.ai_1 == 'Scissors' or 'Lizard':
                print('AI 2 beat AI 1!')
            elif self.ai_2 == 'Paper' and self.ai_1 == 'Rock' or 'Spock':
                print('AI 2 beat AI 1!')
            elif self.ai_2 == 'Scissors' and self.ai_1 == 'Paper' or 'Lizard':
                print('AI 2 beat AI 1!')
            elif self.ai_2 == 'Lizard' and self.ai_1 == 'Spock' or 'Paper':
                print('AI 2 beat AI 1!')
            elif self.ai_2 == 'Spock' and self.ai_1 == 'Scissors' or 'Rock':
                print('AI 2 beat AI 1!')
            else:
                print('AI 2 tied AI 1!')                
        elif self.choose_number_of_players() == 1:
            self.ai_1 = self.ai.choose_options()
            print(f'AI 1 has {self.ai_1}!')
            self.human_1 = self.human.choose_options()
            print(f'Player 1 has {self.human_1}!')
            if self.ai_1 == 'Rock' and self.human_1 == 'Scissors' or 'Lizard':
                print('The AI beat the you!')
            elif self.ai_1 == 'Paper' and self.human_1 == 'Rock' or 'Spock':
                print('The AI beat the you!')
            elif self.ai_1 == 'Scissors' and self.human_1 == 'Paper' or 'Lizard':
                print('The AI beat the you!')
            elif self.ai_1 == 'Lizard' and self.human_1 == 'Spock' or 'Paper':
                print('The AI beat the you!')
            elif self.ai_1 == 'Spock' and self.human_1 == 'Scissors' or 'Rock':
                print('The AI beat the you!')
            elif self.human_1 == 'Rock' and self.ai_1 == 'Scissors' or 'Lizard':
                print('Player 1 beat the AI!')
            elif self.human_1 == 'Paper' and self.ai_1 == 'Rock' or 'Spock':
                print('Player 1 beat the AI!')
            elif self.human_1 == 'Scissors' and self.ai_1 == 'Paper' or 'Lizard':
                print('Player 1 beat the AI!')
            elif self.human_1 == 'Lizard' and self.ai_1 == 'Spock' or 'Paper':
                print('Player 1 beat the AI!')
            elif self.human_1 == 'Spock' and self.ai_1 == 'Scissors' or 'Rock':
                print('Player 1 beat the AI!')
            else:
                print('Player 1 and the AI tied!')
        elif self.choose_number_of_players() == 2:
            self.human_1 = self.human.choose_options()
            print(f'Player 1 has {self.human_1}!')
            self.human_2 = self.human.choose_options()
            print(f'Player 2 has {self.human_2}!')
            if self.human_1 == 'Rock' and self.human_2 == 'Scissors' or 'Lizard':
                print('Player 1 beat the Player 2!')
            elif self.human_1 == 'Paper' and self.human_2 == 'Rock' or 'Spock':
                print('Player 1 beat the Player 2!')
            elif self.human_1 == 'Scissors' and self.human_2 == 'Paper' or 'Lizard':
                print('Player 1 beat the Player 2!')
            elif self.human_1 == 'Lizard' and self.human_2 == 'Spock' or 'Paper':
                print('Player 1 beat the Player 2!')
            elif self.human_1 == 'Spock' and self.human_2 == 'Scissors' or 'Rock':
                print('Player 1 beat the Player 2!')
            elif self.human_2 == 'Rock' and self.human_1 == 'Scissors' or 'Lizard':
                print('Player 2 beat the Player 1!')
            elif self.human_2 == 'Paper' and self.human_1 == 'Rock' or 'Spock':
                print('Player 2 beat the Player 1!')
            elif self.human_2 == 'Scissors' and self.human_1 == 'Paper' or 'Lizard':
                print('Player 2 beat the Player 1!')
            elif self.human_2 == 'Lizard' and self.human_1 == 'Spock' or 'Paper':
                print('Player 2 beat the Player 1!')
            elif self.human_2 == 'Spock' and self.human_1 == 'Scissors' or 'Rock':
                print('Player 2 beat the Player 1!')
            else:
                print('Player 1 and the AI tied!')


    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.choose_number_of_players()
        self.find_winner