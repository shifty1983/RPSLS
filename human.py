from select import select
from player import Player
import getpass

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        i = 0
        for gesture in self.gesture_list:
            print(f'Press {i} to select {gesture}')
            i += 1
        while True:
            self.gesture = getpass.getpass(f'{self.name} select gesture to use for the round. ')
            try:
                self.gesture = int(self.gesture)
            except:
                print('Please user numeric digits.')
                continue
            if self.gesture < 0 or self.gesture > 4:
                print('Please enter a number between 0 and 4.')
                continue
            break
        print()
        return(self.gesture)
