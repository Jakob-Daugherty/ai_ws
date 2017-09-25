from math import fabs
goal_row = dict({1: int(0), 2: int(0), 3: int(0), 4: int(1), 5: int(1), 6: int(1), 7: int(2), 8: int(2)})
goal_col = dict({1: int(0), 2: int(1), 3: int(2), 4: int(0), 5: int(1), 6: int(2), 7: int(0), 8: int(1)})
init1_row = dict({1: int(0), 2: int(1), 3: int(0), 4: int(1), 5: int(1), 6: int(2), 7: int(2), 8: int(2)})
init1_col = dict({1: int(1), 2: int(1), 3: int(2), 4: int(0), 5: int(2), 6: int(2), 7: int(0), 8: int(1)})
init2_row = dict({1: int(1), 2: int(0), 3: int(1), 4: int(2), 5: int(0), 6: int(2), 7: int(2), 8: int(1)})
init2_col = dict({1: int(0), 2: int(2), 3: int(2), 4: int(0), 5: int(1), 6: int(2), 7: int(1), 8: int(1)})
init3_row = dict({1: int(2), 2: int(1), 3: int(2), 4: int(1), 5: int(1), 6: int(0), 7: int(0), 8: int(0)})
init3_col = dict({1: int(2), 2: int(0), 3: int(0), 4: int(2), 5: int(1), 6: int(1), 7: int(2), 8: int(0)})
class eight_puzzle():
    def __init__(self):
        self.free_space_row = -1
        self.free_space_col = -1
        self.board = [[0 for x in range(3)] for y in range(3)]
    def compare_2_states(self, state):
        value = True
        for r in range(3):
            for c in range(3):
                if self.board[r][c] != state.board[r][c]:
                    value = False
        return value
    def goal_test(self):
        test_result = True
        goal = eight_puzzle()
        goal.set_board(0)
        for r in range(3):
            for c in range(3):
                if self.board[r][c] != goal.board[r][c]:
                    test_result = False
        return test_result
    def calc_h_value(self):
        value = 0
        for r in range(3):
            for c in range(3):
                piece = self.board[r][c]
                if piece != '.':
                    goal_r = str(goal_row.get(int(piece)))
                    goal_c = str(goal_col.get(int(piece)))
                    delta_r = r - int(goal_r)
                    delta_c = c - int(goal_c)
                    distance = fabs(delta_r) + fabs(delta_c)
                    value = value + distance
        return value
    def calc_g_value(self, puzzle_choice):
        value = 0
        if puzzle_choice == 1:
            for r in range(3):
                for c in range(3):
                    piece = self.board[r][c]
                    if piece != '.':
                        init_r = str(init1_row.get(int(piece)))
                        init_c = str(init1_col.get(int(piece)))
                        delta_r = r - int(init_r)
                        delta_c = c - int(init_c)
                        distance = fabs(delta_r) + fabs(delta_c)
                        value = value + distance
        if puzzle_choice == 2:
            for r in range(3):
                for c in range(3):
                    piece = self.board[r][c]
                    if piece != '.':
                        init_r = str(init2_row.get(int(piece)))
                        init_c = str(init2_col.get(int(piece)))
                        delta_r = r - int(init_r)
                        delta_c = c - int(init_c)
                        distance = fabs(delta_r) + fabs(delta_c)
                        value = value + distance
        if puzzle_choice == 3:
            for r in range(3):
                for c in range(3):
                    piece = self.board[r][c]
                    if piece != '.':
                        init_r = str(init3_row.get(int(piece)))
                        init_c = str(init3_col.get(int(piece)))
                        delta_r = r - int(init_r)
                        delta_c = c - int(init_c)
                        distance = fabs(delta_r) + fabs(delta_c)
                        value = value + distance
        return value
    def make_child(self):
        child = eight_puzzle()
        for r in range(3):
            for c in range(3):
                child.board[r][c] = self.board[r][c]
                child.free_space_row = self.free_space_row
                child.free_space_col = self.free_space_col
        return child
    def set_board(self, index):
        if index == 0:
            self.free_space_row = 2
            self.free_space_col = 2
            self.board[0][0] = 1
            self.board[0][1] = 2
            self.board[0][2] = 3
            self.board[1][0] = 4
            self.board[1][1] = 5
            self.board[1][2] = 6
            self.board[2][0] = 7
            self.board[2][1] = 8
            self.board[2][2] = '.'
        if index == 1:
            self.free_space_row = 0
            self.free_space_col = 0
            self.board[0][0] = '.'
            self.board[0][1] = 1
            self.board[0][2] = 3
            self.board[1][0] = 4
            self.board[1][1] = 2
            self.board[1][2] = 5
            self.board[2][0] = 7
            self.board[2][1] = 8
            self.board[2][2] = 6
        if index == 2:
            self.free_space_row = 0
            self.free_space_col = 0
            self.board[0][0] = '.'
            self.board[0][1] = 5
            self.board[0][2] = 2
            self.board[1][0] = 1
            self.board[1][1] = 8
            self.board[1][2] = 3
            self.board[2][0] = 4
            self.board[2][1] = 7
            self.board[2][2] = 6
        if index == 3:
            self.free_space_row = 2
            self.free_space_col = 1
            self.board[0][0] = 8
            self.board[0][1] = 6
            self.board[0][2] = 7
            self.board[1][0] = 2
            self.board[1][1] = 5
            self.board[1][2] = 4
            self.board[2][0] = 3
            self.board[2][1] = '.'
            self.board[2][2] = 1
    def print_board(self):
        for row in range(3):
            print self.board[row][0], self.board[row][1], self.board[row][2]
    def possible_moves(self):
        moves_list = []
        if self.free_space_row == 0:
            if self.free_space_col == 0:
                move = self.board[0][1]
                moves_list.append((move))
                move = self.board[1][0]
                moves_list.append((move))
            if self.free_space_col == 1:
                move = self.board[0][0]
                moves_list.append((move))
                move = self.board[0][2]
                moves_list.append((move))
                move = self.board[1][1]
                moves_list.append((move))
            if self.free_space_col == 2:
                move = self.board[0][1]
                moves_list.append((move))
                move = self.board[1][2]
                moves_list.append((move))
        if self.free_space_row == 1:
            if self.free_space_col == 0:
                move = self.board[0][0]
                moves_list.append((move))
                move = self.board[1][1]
                moves_list.append((move))
                move = self.board[2][0]
                moves_list.append((move))
            if self.free_space_col == 1:
                move = self.board[0][1]
                moves_list.append(move)
                move = self.board[1][2]
                moves_list.append(move)
                move = self.board[2][1]
                moves_list.append(move)
                move = self.board[1][0]
                moves_list.append(move)
            if self.free_space_col == 2:
                move = self.board[0][2]
                moves_list.append(move)
                move = self.board[1][1]
                moves_list.append(move)
                move = self.board[2][2]
                moves_list.append(move)
        if self.free_space_row == 2:
            if self.free_space_col == 0:
                move = self.board[1][0]
                moves_list.append(move)
                move = self.board[2][1]
                moves_list.append(move)
            if self.free_space_col == 1:
                move = self.board[2][0]
                moves_list.append(move)
                move = self.board[1][1]
                moves_list.append(move)
                move = self.board[2][2]
                moves_list.append(move)
            if self.free_space_col == 2:
                move = self.board[2][1]
                moves_list.append(move)
                move = self.board[1][2]
                moves_list.append((move))
        return moves_list
    def move(self, value):
        if self.free_space_row == 0:
            if self.free_space_col == 0:
                if self.board[0][1] == value:
                    self.board[0][1] = '.'
                    self.board[0][0] = value
                    self.free_space_col = 1
                    self.free_space_row = 0
                    return True
                if self.board[1][0] == value:
                    self.board[1][0] = '.'
                    self.board[0][0] = value
                    self.free_space_row = 1
                    self.free_space_col = 0
                    return True
            if self.free_space_col == 1:
                if self.board[0][0] == value:
                    self.board[0][0] = '.'
                    self.board[0][1] = value
                    self.free_space_row = 0
                    self.free_space_col = 0
                    return True
                if self.board[1][1] == value:
                    self.board[1][1] = '.'
                    self.board[0][1] = value
                    self.free_space_row = 1
                    self.free_space_col = 1
                    return True
                if self.board[0][2] == value:
                    self.board[0][2] = '.'
                    self.board[0][1] = value
                    self.free_space_row = 0
                    self.free_space_col = 2
                    return True
            if self.free_space_col == 2:
                if self.board[0][1] == value:
                    self.board[0][1] = '.'
                    self.board[0][2] = value
                    self.free_space_row = 0
                    self.free_space_col = 1
                    return True
                if self.board[1][2] == value:
                    self.board[1][2] = '.'
                    self.board[0][2] = value
                    self.free_space_row = 1
                    self.free_space_col = 2
                    return True
        if self.free_space_row == 1:
            if self.free_space_col == 0:
                if self.board[0][0] == value:
                    self.board[0][0] = '.'
                    self.board[1][0] = value
                    self.free_space_row = 0
                    self.free_space_col = 0
                    return True
                if self.board[1][1] == value:
                    self.board[1][1] = '.'
                    self.board[1][0] = value
                    self.free_space_row = 1
                    self.free_space_col = 1
                    return True
                if self.board[2][0] == value:
                    self.board[2][0] = '.'
                    self.board[1][0] = value
                    self.free_space_row = 2
                    self.free_space_col = 0
                    return True
            if self.free_space_col == 1:
                if self.board[0][1] == value:
                    self.board[0][1] = '.'
                    self.board[1][1] = value
                    self.free_space_row = 0
                    self.free_space_col = 1
                    return True
                if self.board[1][2] == value:
                    self.board[1][2] = '.'
                    self.board[1][1] = value
                    self.free_space_row = 1
                    self.free_space_col = 2
                    return True
                if self.board[2][1] == value:
                    self.board[2][1] = '.'
                    self.board[1][1] = value
                    self.free_space_row = 2
                    self.free_space_col = 1
                    return True
                if self.board[1][0] == value:
                    self.board[1][0] = '.'
                    self.board[1][1] = value
                    self.free_space_row = 1
                    self.free_space_col = 0
                    return True
            if self.free_space_col == 2:
                if self.board[0][2] == value:
                    self.board[0][2] = '.'
                    self.board[1][2] = value
                    self.free_space_row = 0
                    self.free_space_col = 2
                    return True
                if self.board[1][1] == value:
                    self.board[1][1] = '.'
                    self.board[1][2] = value
                    self.free_space_row = 1
                    self.free_space_col = 1
                    return True
                if self.board[2][2] == value:
                    self.board[2][2] = '.'
                    self.board[1][2] = value
                    self.free_space_row = 2
                    self.free_space_col = 2
                    return True
        if self.free_space_row == 2:
            if self.free_space_col == 0:
                if self.board[1][0] == value:
                    self.board[1][0] = '.'
                    self.board[2][0] = value
                    self.free_space_row = 1
                    self.free_space_col = 0
                    return True
                if self.board[2][1] == value:
                    self.board[2][1] = '.'
                    self.board[2][0] = value
                    self.free_space_row = 2
                    self.free_space_col = 1
                    return True
            if self.free_space_col == 1:
                if self.board[2][0] == value:
                    self.board[2][0] = '.'
                    self.board[2][1] = value
                    self.free_space_row = 2
                    self.free_space_col = 0
                    return True
                if self.board[1][1] == value:
                    self.board[1][1] = '.'
                    self.board[2][1] = value
                    self.free_space_row = 1
                    self.free_space_col = 1
                    return True
                if self.board[2][2] == value:
                    self.board[2][2] = '.'
                    self.board[2][1] = value
                    self.free_space_row = 2
                    self.free_space_col = 2
                    return True
            if self.free_space_col == 2:
                if self.board[2][1] == value:
                    self.board[2][1] = '.'
                    self.board[2][2] = value
                    self.free_space_row = 2
                    self.free_space_col = 1
                    return True
                if self.board[1][2] == value:
                    self.board[1][2] = '.'
                    self.board[2][2] = value
                    self.free_space_row = 1
                    self.free_space_col = 2
                    return True
        return False