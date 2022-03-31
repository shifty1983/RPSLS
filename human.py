from player import Player
from time import sleep

class Human(Player):
    def __init__(self, name):
        super().__init__(name)