from player import Player
import random
from time import sleep

class AI(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        self.choose_gesture = random.randint(0,4)
        sleep(1)
        print(f'{self.name} has picked {self.gesture_list[self.choose_gesture]}')