import tic_tac_toe_4
from random import randint

def get_user_choice(prompt, low, high):
    display = 'Please enter: ' + prompt + ' '
    while(True):
        try:
            choice = int(input(display))
            if choice < low or choice > high:
                print 'Please pick a value between ', low, ' and ', high
                continue
        except Exception as err:
            print err
            continue
        break
    return choice

def user_move(game):
    row_max = 4
    col_max = 5
    result = False
    while(result == False):
        print
        user_row = get_user_choice('row number', 0, row_max)
        user_col = get_user_choice('column number', 0, col_max)
        print
        result = game.player_move(user_row, user_col)
        if result == False:
            print 'Please try again with different values'
    game.print_board()
    return game

def beginner_set_move(game):
    moves_list = game.find_next_3iar('X')
    if len(moves_list) > 0:
        move = moves_list.pop()
        row,col = move
        print '<----------- row ->', row
        print '<- trying to win ->'
        print '<----------- col ->', col
        if row or col != -1:
            return row,col
    opp_moves_list = game.find_next_3iar('O')
    if len(opp_moves_list) > 0:
        move = opp_moves_list.pop()
        row,col = move
        print '<------------- row ->', row
        print '<- trying to block ->'
        print '<------------- col ->', col
        if row or col != -1:
            return row,col
    else:
        row = randint(0,4)
        col = randint(0,5)
        return row,col


def beginner_move(game):
    result = False
    while(result == False):
        row, col = beginner_set_move(game)
        result = game.player_move(row, col)
    game.print_board()
    return game

def main():
    print '<-------------->'
    print '<- Start Main ->'
    print '<-------------->'
    goal_reached = False
    first_eight = []
    game = tic_tac_toe_4.tic_tac_toe_4()
    while goal_reached == False:



        #game.print_board()
        game = beginner_move(game)
        if len(first_eight) < 8:
            display = game.make_copy()
            first_eight.append(display)
        goal_reached, winner = game.goal_test()
        if winner != None:
            print '<---------->'
            print '<- Winner -> ',winner
            print '<---------->'
            break
        game = user_move(game)
        if len(first_eight) < 8:
            display = game.make_copy()
            first_eight.append(display)
        goal_reached, winner = game.goal_test()
        if winner != None:
            print '<---------->'
            print '<- Winner -> ',winner
            print '<---------->'
            break






    move = 1
    for item in first_eight:
        print '<--> Move #: ', move
        item.print_board()
        print
        move += 1

    print 'Final game state'
    game.print_board()

    print '<------------>'
    print '<- End Main ->'
    print '<------------>'

main()