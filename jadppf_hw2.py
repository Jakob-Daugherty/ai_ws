import eight_puzzle
from collections import deque
from copy import deepcopy
from time import time
from operator import attrgetter


class eight_puzzle_node():

    def __init__(self, puzzle, choice, choiceList, nodeId):
        result = False
        self.puzzle_state = puzzle.make_child()
        if choice != '.':
            result = self.puzzle_state.move(choice)
        self.choiceList = deepcopy(choiceList)
        if result == True:
            self.choiceList.append(choice)
        self.nodeId = nodeId
        self.h_value = -1

    def print_puzzle_state(self):
        self.puzzle_state.print_board()

    def print_choiceList(self):
        print self.choiceList

    def print_nodeId(self):
        print self.nodeId

def i_ds(problem, fringe):
    depthLimit = 1
    while(True):
        print 'the depth is:'
        print depthLimit
        print
        result = dfs_tree(problem, fringe, depthLimit,)

        if result != False:
            if result == -1:
                break
            return result
        depthLimit += 1
        if depthLimit > 100000:
            print '<------------------------->'
            print '<-- Depth limit reached -->'
            print '<------------------------->'
            break
    return False




def dfs_tree(problem, fringe, depthLimit):
    puzzle = problem.make_child()
    list = []
    root = eight_puzzle_node(puzzle, ".", list, 0)
    new_id = 1
    fringe.append(root)
    while(True):
        if len(fringe) == 0:
            return False
        current = fringe.popleft()
        if current.nodeId < 5:
            print '-----'
            print 'node -> ',current.nodeId + 1
            current.puzzle_state.print_board()
            print '-----'

        if current.puzzle_state.goal_test():
            #print '<----------->'
            #print '<-- Depth -->'
            #print depth
            #print '<----------->'
            return current
        expandChoices = current.puzzle_state.possible_moves()
        for choice in expandChoices:
            new_node = eight_puzzle_node(current.puzzle_state, choice, current.choiceList, new_id)
            new_id += 1
            depth = len(new_node.choiceList)
            if depth < depthLimit:
                fringe.append(new_node)
            if new_id > 100000:
                print '<------------------------>'
                print '<-- Node Limit Reached -->'
                print '<------------------------>'
                return -1

def dfgs(problem, fringe):
    closed = deque([])
    puzzle = problem.make_child()
    list = []
    root = eight_puzzle_node(puzzle, '.', list, 0)
    fringe.append(root)
    new_id = 1
    while(True):
        if len(fringe) == 0:
            return False
        current = fringe.popleft()
        if current.nodeId < 5:
            print '-----'
            print 'node -> ',current.nodeId + 1
            current.puzzle_state.print_board()
            print '-----'

        if current.puzzle_state.goal_test():
            return current
        if current.puzzle_state not in closed:
            closed.append(current.puzzle_state)
            expandChoices = current.puzzle_state.possible_moves()
            for choice in expandChoices:
                new_node = eight_puzzle_node(current.puzzle_state, choice, current.choiceList, new_id)
                if new_node.puzzle_state not in closed:
                    new_id += 1
                    fringe.append(new_node)
#                new_id += 1
#                fringe.append(new_node)
                if new_id > 100000:
                    print '<------------------------>'
                    print '<-- Node Limit Reached -->'
                    print '<------------------------>'
                    return False
    return False

def a_star(problem, fringe):
    puzzle = problem.make_child()
    list = []
    closed = []
    root = eight_puzzle_node(puzzle, '.', list, 0)
    new_id = 1
    fringe.append(root)
    counter = 0
    while(True):
        if len(fringe) == 0:
            return False
        current = fringe.pop()
        print current.nodeId
        print current.h_value
        current.puzzle_state.print_board()
        print '--->'
        if counter < 5:
            print '-----'
            print 'node -> ',counter + 1
            current.puzzle_state.print_board()
            print '-----'
            counter += 1
        if current.puzzle_state.goal_test():
            return current
        if current.puzzle_state not in closed:
            closed.append(current.puzzle_state)
            expandChoices = current.puzzle_state.possible_moves()
            for choice in expandChoices:
                new_node = eight_puzzle_node(current.puzzle_state, choice, current.choiceList, new_id)
                new_node.h_value = new_node.puzzle_state.calc_h_value()
                #new_node.h_value = new_node.h_value + new_node.puzzle_state.calc_g_value()
                if new_node.puzzle_state not in closed:
                    fringe.append(new_node)
                    new_id += 1
#                fringe.append(new_node)
#                new_id += 1
                if new_id > 100000:
                    print '<------------------------>'
                    print '<-- Node Limit Reached -->'
                    print '<------------------------>'
                    return False

        fringe.sort(key=lambda eight_puzzle_node: eight_puzzle_node.h_value, reverse=True)
#        sorted(fringe, key=attrgetter('h_value'))
        #for item in unsorted_nodes:
        #    fringe.append(item)









def jadppf_hw2(search_choice, puzzle_choice):
    print '<-------------------->'
    print '<---> Timer Mark <--->'
    mark = int(round(time() * 1000))
    print '<-------------------->'
    game = eight_puzzle.eight_puzzle()
    if puzzle_choice == 1:
        # use board 2
        game.set_board(2)
    if puzzle_choice == 2:
        # use board 3
        game.set_board(3)
    if puzzle_choice == 0:
        # Use board 1
        game.set_board(1)
    game.print_board()
    #possible_moves = game.possible_moves()
    #print
    #print possible_moves
    print '<---------------------->'
    print '<---> Start Search <--->'
    print '<---------------------->'
    result = False
    if search_choice == 1:

        fringe = deque([])
        result = dfgs(game, fringe)
    if search_choice == 2:
        a_star_list = []
    #result = dfs_tree(game, fringe)
    #result = i_ds(game, fringe)
        result = a_star(game, a_star_list)
    if search_choice == 0:
        fringe = deque([])
        result = i_ds(game, fringe)
    if result != False:
        print 'Solution sequence'
        result.print_choiceList()
        print 'number of moves -> ', len(result.choiceList)
        print 'Num Nodes Expanded'
        result.print_nodeId()


    print '<-------------------->'
    print '<---> Timer Mark <--->'
    now = int(round(time() * 1000))
    print '<-------------------->'
    diff = now - mark

    value = str(int(diff)) + ' milli sec'
    print value


def main():
    print '\nWelcome to main\n'
    exit = True
    while(exit):
        search_choice = 0
        while(True):
            print '\nAvailable search methods.'
            print '[1] Iterative Deepening Tree Search'
            print '[2] Depth-First Graph Search'
            print '[3] A* with heuristics\n'
            try:
                search_choice = int(input('Please select search method (1..3) ->\n'))
                if search_choice not in range(1,4):
                    print 'Err: Please select number between 1 and 3 then try again'
                    continue
            except Exception as err:
                print 'Error'
                print err
                continue
            break
        puzzle_choice = 0
        while(True):
            print '\nPuzzle configurations'
            print '[1]'
            demo = eight_puzzle.eight_puzzle()
            demo.set_board(1)
            demo.print_board()
            print '[2]'
            demo.set_board(2)
            demo.print_board()
            print '[3]'
            demo.set_board(3)
            demo.print_board()
            try:
                puzzle_choice = int(input('Please select puzzle configuration (1..3) ->\n'))
                if puzzle_choice not in range(1,4):
                    print 'Err: Please select number between 1 and 3 then try again'
                    continue
            except Exception as err:
                print 'Error'
                print err
                continue
            break
        jadppf_hw2(search_choice - 1, puzzle_choice - 1)
        #again = str(input('\nAgain (y/n)?\n'))
        #if again == 'n':
        #    exit = False








    print '\nEnd main\n'

main()