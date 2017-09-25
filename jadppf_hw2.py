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
        self.g_value = -1
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
    closed = []
    puzzle = problem.make_child()
    list = []
    root = eight_puzzle_node(puzzle, '.', list, 0)
    fringe.append(root)
    new_id = 1
    counter = 0
    first_nodes = []
    while(True):
        if len(fringe) == 0:
            return False, first_nodes
        current = fringe.popleft()
        if counter < 5:
            first_nodes.append(current)
            counter += 1
        if current.puzzle_state.goal_test():
            return current, first_nodes
        cmp_result = False
        for item in closed:
            cmp_result = current.puzzle_state.compare_2_states(item)
            if cmp_result == True:
                break
        if cmp_result == False:
            closed.append(current.puzzle_state)
            expandChoices = current.puzzle_state.possible_moves()
            for choice in expandChoices:
                new_state = current.puzzle_state
                solun = current.choiceList
                new_node = eight_puzzle_node(new_state, choice, solun, new_id)
                new_id += 1
                fringe.append(new_node)
                print 'new id ->', new_node.nodeId
                if new_id > 1000:
                    print '<------------------------>'
                    print '<-- Node Limit Reached -->'
                    print '<------------------------>'
                    return False, first_nodes
    return False,first_nodes
def a_star(problem, fringe, puzzle_choice):
    puzzle = problem.make_child()
    list = []
    closed = []
    root = eight_puzzle_node(puzzle, '.', list, 0)
    new_id = 1
    fringe.append(root)
    counter = 0
    first_nodes = []
    while(True):
        if len(fringe) == 0:
            return False
        current = fringe.pop()
        current.h_value = current.puzzle_state.calc_h_value()
        current.g_value = current.puzzle_state.calc_g_value(puzzle_choice)
        if counter < 5:
            first_nodes.append(current)
            counter += 1
        if current.puzzle_state.goal_test():
            return current, first_nodes
        cmp_result = False
        for item in closed:
            cmp_result = current.puzzle_state.compare_2_states(item)
            if cmp_result == True:
                break
        if cmp_result == False:
            closed.append(current.puzzle_state)
            expandChoices = current.puzzle_state.possible_moves()
            print expandChoices
            for choice in expandChoices:
                puzzle = current.puzzle_state.make_child()
                solun = current.choiceList
                new_node = eight_puzzle_node(puzzle, choice, solun, new_id)
                new_node.h_value = new_node.puzzle_state.calc_h_value()
                new_node.g_value = new_node.puzzle_state.calc_g_value(puzzle_choice)
                fringe.append(new_node)
                new_id += 1
                print 'expand on ->', choice
                if new_id > 100000:
                    print '<------------------------>'
                    print '<-- Node Limit Reached -->'
                    print '<------------------------>'
                    return False, first_nodes
        fringe.sort(key=attrgetter('h_value'), reverse=True)
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
    print '<---------------------->'
    print '<---> Start Search <--->'
    print '<---------------------->'
    result = False
    first_nodes = None
    if search_choice == 1:
        fringe = deque([])
        result, first_nodes = dfgs(game, fringe)
    if search_choice == 2:
        a_star_list = []
        result, first_nodes = a_star(game, a_star_list, puzzle_choice + 1)
    if search_choice == 0:
        fringe = deque([])
        result = i_ds(game, fringe)
    if result != False:
        result.puzzle_state.print_board()
        print 'Solution sequence'
        result.print_choiceList()
        print 'number of moves -> ', len(result.choiceList)
        print 'Num Nodes Expanded'
        result.print_nodeId()
    if first_nodes != None:
        counter = 0
        for item in first_nodes:
            print 'node ->', counter
            item.puzzle_state.print_board()
            counter += 1
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
    print '\nEnd main\n'
main()