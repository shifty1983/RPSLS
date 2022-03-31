from matplotlib.pyplot import cla
from human import Human
from ai import AI
from time import sleep

class Game():
    def __init__(self):
        pass

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissor, Lizard, Spock.')
        sleep(1)
        print('Each match will be the best of three games.')
        sleep(1)
        print('Number keys will be used to make gesture selections.')
        sleep(1)
        print('Rules of the game.')
        for rule in self.rules_list:
            print(rule)
            sleep(1)