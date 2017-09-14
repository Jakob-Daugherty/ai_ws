import eight_puzzle
from collections import deque
from copy import deepcopy
from time import time

class eight_puzzle_node():

    def __init__(self, puzzle, choice, choiceList, nodeId):
        self.puzzle_state = puzzle.make_child()
        if choice != '.':
            self.puzzle_state.move(choice)
        self.choiceList = deepcopy(choiceList)
        if choice != ".":
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
        result = dfs_tree(problem, fringe, depthLimit)

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
  #      if current.nodeId < 5:
  #          print '-----'
  #          print current.nodeId
  #          print '-----'
  #          current.puzzle_state.print_board()
  #          print '-----'
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
            print current.nodeId
            print '-----'
            current.puzzle_state.print_board()
            print '-----'
        if current.puzzle_state.goal_test():
            return current
        if current not in closed:
            closed.append(current)
            expandChoices = current.puzzle_state.possible_moves()
            for choice in expandChoices:
                new_node = eight_puzzle_node(current.puzzle_state, choice, current.choiceList, new_id)
                new_id += 1
                fringe.append(new_node)
                if new_id > 100000:
                    print '<------------------------>'
                    print '<-- Node Limit Reached -->'
                    print '<------------------------>'
                    return False
    return False

def a_star(problem, fringe):
    puzzle = problem.make_child()
    list = []
    #unsorted_nodes = []
    root = eight_puzzle_node(puzzle, '.', list, 0)
    new_id = 1
    fringe.append(root)
    while(True):
        if len(fringe) == 0:
            return False
        current = fringe.pop()
        print '<---->'
        print current.nodeId
        print current.h_value
        print '<---->'
        if current.puzzle_state.goal_test():
            return current
        expandChoices = current.puzzle_state.possible_moves()
        for choice in expandChoices:
            new_node = eight_puzzle_node(current.puzzle_state, choice, current.choiceList, new_id)
            new_id += 1
            #unsorted_nodes.append(new_node)
            fringe.append(new_node)
            if new_id > 100000:
                print '<------------------------>'
                print '<-- Node Limit Reached -->'
                print '<------------------------>'
                return False
        for item in fringe:
            item.h_value = item.puzzle_state.calc_h_value()
        fringe.sort(key=lambda eight_puzzle_node: eight_puzzle_node.h_value, reverse=True)
        #for item in unsorted_nodes:
        #    fringe.append(item)









def main():
    print '<-------------------->'
    print '<---> Timer Mark <--->'
    mark = time()
    print '<-------------------->'

    print("\nWelcome to main\n")
    game = eight_puzzle.eight_puzzle()
    # Use board 1
    #game.set_board(1)
    # use board 2
    game.set_board(2)
    # use board 3
    #game.set_board(3)
    game.print_board()
    possible_moves = game.possible_moves()
    print
    print possible_moves
    print '<---------------------->'
    print '<---> Start Search <--->'
    print '<---------------------->'
    fringe = deque([])
    a_star_list = []
    #result = dfs_tree(game, fringe)
    #result = i_ds(game, fringe)
    #result = dfgs(game, fringe)
    result = a_star(game, a_star_list)
    if result != False:
        result.print_choiceList()
        result.print_nodeId()


    print '<-------------------->'
    print '<---> Timer Mark <--->'
    now = time()
    print '<-------------------->'
    diff = now - mark
    min = diff // 60
    hr = diff // 3600
    if hr > 0:
        value = str(int(hr)) + ' hr'
        print value
    elif min > 0:
        value = str(int(min)) + ' min'
        print value
    else:
        value = str(int(diff)) + ' sec'
        print value

    print("\nEnd main")

main()