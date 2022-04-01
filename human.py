from player import Player
from time import sleep

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        i = 0
        for gesture in self.gesture_list:
            print(f'Press {i} to select {gesture}')
            i += 1
        self.choose_gesture = int(input("Select gesture to use for the round. "))
        print()
        print(f'{self.name} has picked {self.gesture_list[self.choose_gesture]}\n')
        sleep(1)
        return(self.choose_gesture)
