

class eight_puzzle():


    def __init__(self):
        self.free_space_row = -1
        self.free_space_col = -1
        self.board = [[0 for x in range(3)] for y in range(3)]


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
