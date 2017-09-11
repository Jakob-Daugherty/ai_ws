import eight_puzzle

def main():
    print("\nWelcome to main\n")
    game = eight_puzzle.eight_puzzle()
    game.set_board(1)
    game.print_board()
    possible_moves = game.possible_moves()
    print
    print possible_moves

    game1 = game.make_child()


    result = game.move(possible_moves[0])

    if result != False:
        print
        game.print_board()
        print "\nGoal test"
        print game.goal_test()
        print
        print "Possible moves "
        print game.possible_moves()

    result = game1.move(possible_moves[1])


    if result != False:
        print
        game1.print_board()
        print "\nGoal test"
        print game.goal_test()
        print
        print "possible moves"
        print game1.possible_moves()



    print("\nEnd main")

main()