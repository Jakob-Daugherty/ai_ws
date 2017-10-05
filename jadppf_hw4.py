import tic_tac_toe_4
from random import randint
from decimal import Decimal

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

def max_value(game):
    if game.goal_test():
        return game.utility()
    v = Decimal('Infinity')
    v = -v
    actions_list = game.possible_moves()
    for a in actions_list:
        cur_r,cur_c,cur_v = a
        state_game = game.make_copy()
        move_result = state_game.player_move(r,c)
        if move_result:
            cur_v = state_game.utility()
            a = cur_r,cur_c,cur_v
    for a in actions_list:
        cur_r, cur_c, cur_v = a
        if cur_v > v:
            v = cur_v
    return v

def min_value(game):

    if game.goal_test():
        return game.utility()
    v = Decimal('Infinity')
    actions_list = game.possible_moves()
    for a in actions_list:
        cur_r, cur_c, cur_v = a
        state_game = game.make_copy()
        move_result = state_game.player_move(cur_r, cur_c)
        if move_result:
            cur_v = max_value(game)
            a = cur_r, cur_c, cur_v
    for a in actions_list:
        cur_r, cur_c, cur_v = a
        if cur_v < v:
            v = cur_v
    return v




def minimax_decision(game):
    actions_list = game.possible_moves()
    max_r = 0
    max_c = 0
    max_v = 0
    for a in actions_list:
        cur_r, cur_c, cur_v = a
        result_game = game.make_copy()
        result = result_game.player_move(cur_r, cur_c)
        if result:
            cur_v = min_value(game)
            a = cur_r, cur_c, cur_v
    for a in actions_list:
        cur_r, cur_c, cur_v = a
        if cur_v > max_v:
            max_r = cur_r
            max_c = cur_c
            max_v = cur_v
    print '<----------->'
    print '<- h value -> ', max_v
    print '<----------->'
    return max_r,max_c




def advanced_move(game):
    result = False
    decision_game = game.make_copy()
    while(result == False):

        adv_r, adv_c = minimax_decision(decision_game)
        result = game.player_move(adv_r, adv_c)
        if result == False:
            adv_r = randint(0,4)
            adv_c = randint(0,5)
            result = game.player_move(adv_r,adv_c)
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
        game = advanced_move(game)
        if len(first_eight) < 8:
            display = game.make_copy()
            first_eight.append(display)
        goal_reached, winner = game.goal_test()
        if winner != None:
            print '<---------->'
            print '<- Winner -> ',winner
            print '<---------->'
            break
        choice = get_user_choice('a number',0,9)







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