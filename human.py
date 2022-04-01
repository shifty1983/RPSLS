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
        self.gesture = int(getpass.getpass("Select gesture to use for the round. "))
        return(self.gesture)
