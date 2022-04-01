from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.gesture = random.randint(0,4)
        return(self.gesture)