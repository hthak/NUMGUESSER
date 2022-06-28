from methods import NumberGame


g1 = NumberGame(100, 1000, 101, 100, "easy")
g1.choose_diff()
print('\033[35m')
print("Welcome to NUMGUESSER...\nTo play, guess a number between 0 and " + str(g1.print_diff()) + "\nLET'S PLAY!!!")
g1.set_num()
while not g1.loss():
    g1.make_guess()
    g1.update_score()
    g1.evaluate_guess()
    if not g1.loss():
        print("GUESS AGAIN!")
print('\033[31m')
print("YOU LOST! DON'T BE SAD, PLAY AGAIN!!")
