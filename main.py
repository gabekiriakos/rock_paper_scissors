from game import Game

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
