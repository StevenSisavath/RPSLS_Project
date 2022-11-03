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
        player_1_count = 0
        player_2_count = 0
        necessary_wins = 2
        game_continues = True
        if self.number_of_players == 0:
            while game_continues:
                self.player_1 = self.ai.choose_options()
                self.player_2 = self.ai.choose_options()
                print(f'AI 1 has {self.player_1}!')
                print(f'AI 2 has {self.player_2}!')
                if self.player_1 == 'Rock':
                    if self.player_2 == 'Scissors' or self.player_2 == 'Lizard':
                        print('AI 1 beat the AI 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('AI 1 wins')                                                    
                    elif self.player_2 == 'Paper' or self.player_2 == 'Spock':
                        print('AI 2 beat the AI 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI 2 wins')                          
                    elif self.player_2 == 'Rock':
                        print('AI 1 tied AI 2!')

                elif self.player_1 == 'Scissors':
                    if self.player_2 == 'Paper' or self.player_2 == 'Lizard':
                        print('AI 1 beat the AI 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('AI 1 wins')  
                            return
                    elif self.player_2 == 'Rock' or self.player_2 == 'Spock':
                        print('AI 2 beat the AI 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI 2 wins')
                    elif self.player_2 == 'Scissors':
                        print('AI 1 tied AI 2!')

                elif self.player_1 == 'Paper':
                    if self.player_2 == 'Rock' or self.player_2 == 'Spock':
                        print('AI 1 beat the AI 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('AI 1 wins')  
                    elif self.player_2 == 'Lizard' or self.player_2 == 'Scissors':
                        print('AI 2 beat the AI 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI 2 wins')
                    elif self.player_2 == 'Paper':
                        print('AI 1 tied AI 2!')

                elif self.player_1 == 'Lizard':
                    if self.player_2 == 'Paper' or self.player_2 == 'Spock':
                        print('AI 1 beat the AI 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('AI 1 wins')  
                    elif self.player_2 == 'Scissors' or self.player_2 == 'Rock':
                        print('AI 2 beat the AI 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI 2 wins')
                    elif self.player_2 == 'Lizard':
                        print('AI 1 tied AI 2!')

                elif self.player_1 == 'Spock':
                    if self.player_2 == 'Rock' or self.player_2 == 'Scissors':
                        print('AI 1 beat the AI 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('AI 1 wins')  
                    elif self.player_2 == 'Lizard' or self.player_2 == 'Paper':
                        print('AI 2 beat the AI 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI 2 wins')
                    elif self.player_2 == 'Spock':
                        print('AI 1 tied AI 2!') 


        elif self.number_of_players == 1:
            while game_continues:
                self.player_1 = self.human.choose_options()
                self.player_2 = self.ai.choose_options()
                print(f'Player 1 has {self.player_1}!')
                print(f'AI 1 has {self.player_2}!')
                if self.player_1 == 'Rock':
                    if self.player_2 == 'Scissors' or self.player_2 == 'Lizard':
                        print('Player 1 beat the AI!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')                                                    
                    elif self.player_2 == 'Paper' or self.player_2 == 'Spock':
                        print('The AI beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI wins')                           
                    elif self.player_2 == 'Rock':
                        print('Player 1 tied the AI!') 

                elif self.player_1 == 'Scissors':
                    if self.player_2 == 'Paper' or self.player_2 == 'Lizard':
                        print('Player 1 beat the AI!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')
                            return
                    elif self.player_2 == 'Rock' or self.player_2 == 'Spock':
                        print('The AI beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI wins') 
                    elif self.player_2 == 'Scissors':
                        print('Player 1 tied the AI!')  

                elif self.player_1 == 'Paper':
                    if self.player_2 == 'Rock' or self.player_2 == 'Spock':
                        print('Player 1 beat the AI!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')
                    elif self.player_2 == 'Lizard' or self.player_2 == 'Scissors':
                        print('The AI beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI wins') 
                    elif self.player_2 == 'Paper':
                        print('Player 1 tied the AI!') 

                elif self.player_1 == 'Lizard':
                    if self.player_2 == 'Paper' or self.player_2 == 'Spock':
                        print('Player 1 beat the AI!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')
                    elif self.player_2 == 'Scissors' or self.player_2 == 'Rock':
                        print('The AI beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI wins') 
                    elif self.player_2 == 'Lizard':
                        print('Player 1 tied the AI!') 

                elif self.player_1 == 'Spock':
                    if self.player_2 == 'Rock' or self.player_2 == 'Scissors':
                        print('Player 1 beat the AI!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')
                    elif self.player_2 == 'Lizard' or self.player_2 == 'Paper':
                        print('The AI beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('AI wins') 
                    elif self.player_2 == 'Spock':
                        print('Player 1 tied the AI!') 


        elif self.number_of_players == 2:
            while game_continues:
                self.player_1 = self.human.choose_options()
                self.player_2 = self.human.choose_options()
                print(f'Player 1 has {self.player_1}!')
                print(f'Player 2 has {self.player_2}!')
                if self.player_1 == 'Rock':
                    if self.player_2 == 'Scissors' or self.player_2 == 'Lizard':
                        print('Player 1 beat the Player 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')                                                    
                    elif self.player_2 == 'Paper' or self.player_2 == 'Spock':
                        print('Player 2 beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('Player 2 wins')                           
                    elif self.player_2 == 'Rock':
                        print('Player 1 tied Player 2!')

                elif self.player_1 == 'Scissors':
                    if self.player_2 == 'Paper' or self.player_2 == 'Lizard':
                        print('Player 1 beat the Player 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')
                            return
                    elif self.player_2 == 'Rock' or self.player_2 == 'Spock':
                        print('Player 2 beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('Player 2 wins')
                    elif self.player_2 == 'Scissors':
                        print('Player 1 tied Player 2!') 

                elif self.player_1 == 'Paper':
                    if self.player_2 == 'Rock' or self.player_2 == 'Spock':
                        print('Player 1 beat the Player 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')
                    elif self.player_2 == 'Lizard' or self.player_2 == 'Scissors':
                        print('Player 2 beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('Player 2 wins')
                    elif self.player_2 == 'Paper':
                        print('Player 1 tied Player 2!') 

                elif self.player_1 == 'Lizard':
                    if self.player_2 == 'Paper' or self.player_2 == 'Spock':
                        print('Player 1 beat the Player 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')
                    elif self.player_2 == 'Scissors' or self.player_2 == 'Rock':
                        print('Player 2 beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('Player 2 wins')
                    elif self.player_2 == 'Lizard':
                        print('Player 1 tied Player 2!') 

                elif self.player_1 == 'Spock':
                    if self.player_2 == 'Rock' or self.player_2 == 'Scissors':
                        print('Player 1 beat the Player 2!')
                        player_1_count += 1
                        if player_1_count == necessary_wins:
                            print('Player 1 wins')
                    elif self.player_2 == 'Lizard' or self.player_2 == 'Paper':
                        print('Player 2 beat the Player 1!')
                        player_2_count += 1
                        if player_2_count == necessary_wins:
                            print('Player 2 wins')
                    elif self.player_2 == 'Spock':
                        print('Player 1 tied Player 2!') 
                
    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.determine_winner()