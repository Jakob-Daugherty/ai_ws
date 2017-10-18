import tic_tac_toe_4
from random import randint
import operator

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
        three_iar = moves_list.pop()
        three_iar.print_3iar()
        move = three_iar.get_open_as_index()
        row,col = move
        print '<----------- row ->', row
        print '<- trying to win ->'
        print '<----------- col ->', col
        if row or col != -1:
            return row,col
    opp_moves_list = game.find_next_3iar('O')
    if len(opp_moves_list) > 0:
        three_iar = opp_moves_list.pop()
        three_iar.print_3iar()
        move = three_iar.get_open_as_index()
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

def adv_max_value(game, node_count):
    if game.goal_test():
        return game.utility(), node_count
    actions_list = game.possible_moves()
    for a in actions_list:
        cur_r,cur_c,cur_v = a
        state_game = game.make_copy()
        node_count += 1
        move_result = state_game.player_move(r,c)
        if move_result:
            cur_v = state_game.utility()
            a = cur_r,cur_c,cur_v
    actions_list.sort(key=operator.itemgetter(2))
    item = actions_list.pop()
    r,c,v = item
    return v, node_count

def adv_min_value(game, node_count):

    if game.goal_test():
        return game.utility(), node_count
    actions_list = game.possible_moves()
    for a in actions_list:
        cur_r, cur_c, cur_v = a
        state_game = game.make_copy()
        node_count += 1
        move_result = state_game.player_move(cur_r, cur_c)
        if move_result:
            cur_v, node_count = adv_max_value(state_game, node_count)
            a = cur_r, cur_c, cur_v
    actions_list.sort(key=operator.itemgetter(2))
    item = actions_list(0)
    r,c,v = item
    return v, node_count




def adv_minimax_decision(game, node_count):
    actions_list = game.possible_moves()
    max_r = 0
    max_c = 0
    max_v = 0
    for a in actions_list:
        cur_r, cur_c, cur_v = a
        result_game = game.make_copy()
        node_count += 1
        result = result_game.player_move(cur_r, cur_c)
        if result:
            cur_v, node_count = adv_min_value(result_game,node_count)
            a = cur_r, cur_c, cur_v
    actions_list.sort(key=operator.itemgetter(2))

    return actions_list, node_count




def advanced_move(game):
    node_count = 0
    result = False
    decision_game = game.make_copy()
    node_count += 1
    decisions_list, node_count = adv_minimax_decision(decision_game, node_count)
    while(result == False):
        decision = decisions_list.pop()
        adv_r, adv_c, v = decision
        print '<----------->'
        print '<- h value -> ', v
        print '<----------->'
        if v == 0:
            adv_r = randint(0,4)
            adv_c = randint(0,5)
        result = game.player_move(adv_r, adv_c)
    game.print_board()
    return game, node_count

def master_max2_value(game, node_count):
    if game.goal_test():
        return game.utility(), node_count
    actions_list = game.possible_moves()
    for a in actions_list:
        r,c,v = a
        result_game = game.make_copy()
        node_count += 1
        result = result_game.player_move(r,c)
        if result:
            v = result_game.utility()
            a = r,c,v
    actions_list.sort(key=operator.itemgetter(2))
    item = actions_list.pop()
    r,c,v = item
    return v, node_count

def master_min2_value(game, node_count):
    if game.goal_test():
        return game.utility(), node_count
    actions_list = game.possible_moves()
    for a in actions_list:
        r,c,v = a
        result_game = game.make_copy()
        node_count += 1
        result = result_game.player_move(r,c)
        if result:
            v, node_count = master_max2_value(result_game, node_count)
            a = r,c,v
    actions_list.sort(key=operator.itemgetter(2))
    item = actions_list(0)
    r,c,v = item
    return v, node_count

def master_max1_value(game, node_count):
    if game.goal_test():
        return game.utility(), node_count
    actions_list = game.possible_moves()
    for a in actions_list:
        r,c,v = a
        result_game = game.make_copy()
        node_count += 1
        result = result_game.player_move(r,c)
        if result:
            v, node_count = master_min2_value(result_game, node_count)
            a = r,c,v
    actions_list.sort(key=operator.itemgetter(2))
    item = actions_list.pop()
    r,c,v = item
    return v, node_count

def master_min1_value(game, node_count):
    if game.goal_test():
        return game.utility(), node_count
    actions_list = game.possible_moves()
    for a in actions_list:
        r,c,v = a
        result_game = game.make_copy()
        node_count += 1
        result = result_game.player_move(r,c)
        if result:
            v, node_count = master_max1_value(result_game, node_count)
            a = r,c,v
    actions_list.sort(key=operator.itemgetter(2))
    item = actions_list(0)
    r,c,v = item
    return v, node_count

def master_minimax_decision(game, node_count):
    actions_list = game.possible_moves()
    for a in actions_list:
        r,c,v = a
        result_game = game.make_copy()
        node_count += 1
        result = result_game.player_move(r,c)
        if result:
            v, node_count = master_min1_value(result_game, node_count)
            a = r,c,v
    actions_list.sort(key=operator.itemgetter(2))
    return actions_list, node_count


def master_move(game):
    node_count = 0
    result = False
    decision_game = game.make_copy()
    node_count += 1
    decisions_list, node_count = master_minimax_decision(decision_game, node_count)
    while result == False:
        decision = decisions_list.pop()
        master_r, master_c, v = decision
        print '<----------->'
        print '<- h value -> ', v
        print '<----------->'
        result = game.player_move(master_r,master_c)
    game.print_board()
    return game, node_count


def main():
    from time import time
    ncount_time = []
    master_time = []
    print '<-------------->'
    print '<- Start Main ->'
    print '<-------------->'
    goal_reached = False
    first_eight = []
    game = tic_tac_toe_4.tic_tac_toe_4()
    while goal_reached == False:

        print '<------------------->'
        print '<--- TIMER START --->'
        value = time()
        mark = int(round(value * 1000))
        print '<------------------->'
        #game.print_board()
        game, node_count = user_move(game)
        print '<------------------->'
        print '<--- Timer Finish -->'
        now = int(round(time() * 1000))
        print '<------------------->'
        diff = now - mark
        value = str(int(diff))
        item = node_count, value
        ncount_time.append(item)
        if len(first_eight) < 8:
            display = game.make_copy()
            first_eight.append(display)
        goal_reached, winner = game.goal_test()
        if winner != None:
            print '<---------->'
            print '<- Winner -> ',winner
            print '<---------->'
            break
        #game = master_move(game)

        print '<------------------->'
        print '<--- TIMER START --->'
        value = time()
        mark = int(round(value * 1000))
        print '<------------------->'


        game, node_count = beginner_move(game)
        #game = user_move(game)

        print '<------------------->'
        print '<--- Timer Finish -->'
        now = int(round(time() * 1000))
        print '<------------------->'
        diff = now - mark
        value = str(int(diff))
        item = node_count, value
        master_time.append(item)


        if len(first_eight) < 8:
            display = game.make_copy()
            first_eight.append(display)
        goal_reached, winner = game.goal_test()
        if winner != None:
            print '<---------->'
            print '<- Winner -> ',winner
            print '<---------->'
            break
        #choice = get_user_choice('a number',0,9)







    move = 1
    for item in first_eight:
        print '<--> Move #: ', move
        item.print_board()
        print
        move += 1

    print 'Final game state'
    game.print_board()

    print
    print
    count = 1
    for item in ncount_time:
        n_count, time = item
        print 'Move-> ', count, ' node_count-> ', n_count, ' in time-> ', time, ' millisec'
        count += 1

    print
    print
    count = 1
    for item in master_time:
        n_count, time = item
        print 'Move-> ', count, ' node_count-> ', n_count, ' in time-> ', time, ' millisec'
        count += 1

    print '<------------>'
    print '<- End Main ->'
    print '<------------>'

main()