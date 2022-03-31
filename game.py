from math import gamma
from human import Human
from ai import AI
from time import sleep

class Game():
    def __init__(self):
        self.rules_list = ['Rock crushes Scissors', 'Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock',
                            'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper']

    def display_welcome(self):
        print('\nWelcome to Rock, Paper, Scissor, Lizard, Spock.\n')
        sleep(1)
        print('Each match will be the best of three games.\n')
        sleep(1)
        print('Number keys will be used to make gesture selections.\n')
        sleep(1)
        print('Rules of the game.')
        for rule in self.rules_list:
            print(rule)
            sleep(1)
    
    def choose_players(self):
        self.number_of_players = int(input("\nHow many players? 1, 2, or 3 for a suprise. "))
        print()
        if self.number_of_players == 1:
            name = input('Player 1 enter your name: ')
            self.player1 = Human(name)
            self.player2 = AI('NPC1')
        elif self.number_of_players == 2:
            name = input('Player 1 enter your name: ')
            self.player1 = Human(name)
            name = input('Player 2 enter your name: ')
            self.player2 = Human(name)
        elif self.number_of_players == 3:
            self.player1 = AI('NPC1')
            self.player2 = AI('NPC2')

