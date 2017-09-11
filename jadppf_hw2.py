

import eight_puzzle

def main():
    print("\nWelcome to main\n")
    game = eight_puzzle.eight_puzzle()
    game.set_board(1)
    game.print_board()
    possible_moves = game.possible_moves()
    print
    print possible_moves

    result = game.move(possible_moves[0])
    if result != False:
        print
        game.print_board()

    possible_moves = game.possible_moves()
    print
    print possible_moves
    result = game.move(possible_moves[-1])
    if result != False:
        print
        game.print_board()

    print("\nEnd main")

main()