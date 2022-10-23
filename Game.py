import random
from os import system, name

class Game:
    # constructor
    def __init__(self):
        self.gamer_score = 0
        self.opponent_score = 0
        self.rock = 'rock'
        self.paper = 'paper'
        self.scissors = 'scissors'
        self.is_playing_game = True
        self.opponent_response = ''

    def in_game(self):
        return self.is_playing_game

    def get_opponent_response(self):
        self.opponent_response = random.choice([self.rock, self.paper, self.scissors])
        return self.opponent_response

    def make_comparison(self, choice):
        if (choice == 'R'):
            choice = 'rock'
        elif (choice == 'P'):
            choice = 'paper'
        else:
            choice = 'scissors'

        self.get_opponent_response()

        print('You chose ' + choice)
        print('Your opponent chose ' + self.opponent_response)
        if ((choice == self.rock and self.opponent_response == self.rock) or
            (choice == self.paper and self.opponent_response == self.paper) or
            (choice == self.scissors and self.opponent_response == self.scissors)):
            self.draw()

        # Win scenarios
        if (choice == self.rock and self.opponent_response == self.scissors):
            self.win()
        if (choice == self.scissors and self.opponent_response == self.paper):
            self.win()
        if (choice == self.paper and self.opponent_response == self.rock):
            self.win()

        # Lose scenarios
        if (self.opponent_response == self.rock and choice == self.scissors):
            self.lose()
        if (self.opponent_response == self.scissors and choice == self.paper):
            self.lose()
        if (self.opponent_response == self.paper and choice == self.rock):
            self.lose()

    def draw(self):
        print("Draw!")

    def lose(self):
        print("Opponent Wins!")
        self.opponent_score += 1

    def win(self):
        self.gamer_score += 1
        print("You win!")
    
    def show_score(self):
        print("Current scoreboard")
        print("Your score: {}" .format(self.gamer_score))
        print("Opponent score: {}" .format(self.opponent_score))
    
    def prompt_continue(self):
        print("Continue?")
        decision = input("[Y]es or [No] ").upper()

        while (True):
            if (decision == 'Y'):
                break
            elif (decision == 'N'):
                self.is_playing_game = False
                break
            else:
                decision = input("Please press [Y]es to continue or [N]o quit... ").upper()
                continue

    def clear(self):
        if name == 'nt':
            _ = system('cls') # windows
        else:
            _ = system('clear') # linux, mac

if __name__ == '__main__':

    game = Game()

    while game.in_game():
        game.clear()
        print("[R]ock, [P]aper, or [S]cissors?")
        print("Press a letter representing your choice...")
        choice = input("What is your choice? ")
        choice = choice.upper()

        if any([choice == 'R', choice == 'P', choice == 'S']):
            game.clear()
            game.make_comparison(choice)
            game.show_score()
            game.prompt_continue()
        else:
            game.clear()
            print("[R]ock, [P]aper, or [S]cissors?")
            print("Please enter legitimate choice")
            continue

    print("Thank you for playing!")
    input("Press [ENTER] to exit.")