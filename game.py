from human import Human
from ai import AI
from time import sleep


class Game():
    def __init__(self):
        self.rules_list = ['Rock crushes Scissors', 'Scissors cuts Paper', 'Paper covers Rock', 'Rock crushes Lizard', 'Lizard poisons Spock',
                            'Spock smashes Scissors', 'Scissors decapitates Lizard', 'Lizard eats Paper', 'Paper disproves Spock', 'Spock vaporizes Rock']

    def run_game(self):
        self.display_welcome()
        self.choose_players()
        run = True
        while run == True:
            self.game()
            if self.player1.score == 2 or self.player2.score == 2:
                run = False
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to Rock, Paper, Scissor, Lizard, Spock.\n')
        sleep(1)
        print('Each match will be the best of three rounds.\n')
        sleep(1)
        print('Number keys will be used to make gesture selections.\n')
        sleep(1)
        print('Rules of the game.')
        for rule in self.rules_list:
            print(rule)
    
    def choose_players(self):
        while True:
            self.number_of_players = input("\nHow many players? 1, 2, or 3 for a suprise. ")
            try:
                self.number_of_players = int(self.number_of_players)
            except:
                print('Please user numeric digits.')
                continue
            if self.number_of_players < 1 or self.number_of_players > 3:
                print('Please enter a number between 1 and 3.')
                continue
            break
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
        return(self.player1, self.player2)

    def game(self):
            self.player1_choice = self.player1.choose_gesture()
            self.player2_choice = self.player2.choose_gesture()
            print(f'{self.player1.name} has picked {self.player1.gesture_list[self.player1_choice]}')
            print(f'{self.player2.name} has picked {self.player2.gesture_list[self.player2_choice]}\n')
            sleep(1)
            self.game_outcome(self.player1_choice, self.player2_choice)

    def game_outcome(self, gesture1, gesture2):
        if gesture1 == gesture2:
            print('There are no ties play again.')
        elif ((gesture1 == 0  and (gesture2 == 2 or gesture2 == 3)) or
              (gesture1 == 1  and (gesture2 == 0 or gesture2 == 4)) or 
              (gesture1 == 2  and (gesture2 == 1 or gesture2 == 3)) or 
              (gesture1 == 3  and (gesture2 == 1 or gesture2 == 4)) or 
              (gesture1 == 4  and (gesture2 == 0 or gesture2 == 2))):
                print(f'{self.player1.gesture_list[gesture1]} beats {self.player2.gesture_list[gesture2]}, {self.player1.name} wins the round!\n')
                self.player1.score += 1
        elif ((gesture2 == 0  and (gesture1 == 2 or gesture1 == 3)) or
              (gesture2 == 1  and (gesture1 == 0 or gesture1 == 4)) or 
              (gesture2 == 2  and (gesture1 == 1 or gesture1 == 3)) or 
              (gesture2 == 3  and (gesture1 == 1 or gesture1 == 4)) or 
              (gesture2 == 4  and (gesture1 == 0 or gesture1 == 2))):
                print(f'{self.player2.gesture_list[gesture2]} beats {self.player1.gesture_list[gesture1]}, {self.player2.name} wins the round!\n')
                self.player2.score += 1
        sleep(1)
        print(f'{self.player1.name} score is {self.player1.score}')
        print(f'{self.player2.name} score is {self.player2.score}\n')
        sleep(1)


    def display_winner(self):
        if self.player1.score == 2:
            print(f'{self.player1.name} is the winner!')
        elif self.player2.score == 2:
            print(f'{self.player2.name} is the winner!')
if __name__ == "__main__":
    game = Game()
    game.run_game()