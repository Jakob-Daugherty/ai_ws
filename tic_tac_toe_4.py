

class tic_tac_toe_4():

    def __init__(self):
        # This is a 5x6 2D array filled initially with _ values
        self.board = [['_' for x in range(6)] for y in range(5)]
        # The next move will be made by
        self.next_move = 'X'

    def make_copy(self):
        copy = tic_tac_toe_4()
        for r in range(5):
            for c in range(6):
                copy.board[r][c] = self.board[r][c]
        copy.next_move = self.next_move
        return copy

    def possible_moves(self):
        possible_list = []
        v = 0
        for r in range(5):
            for c in range(6):
                if self.board[r][c] == '_':
                    index = r,c,v
                    possible_list.append(index)
        return possible_list

    def utility(self):
        p = self.find_next_3iar('O')
        q = self.find_next_3iar('X')
        r = self.find_next_2iar('O')
        t = self.find_next_2iar('X')

        h = 3 * len(p) - 3 * len(q) + len(r) - len(t)

        return h



    def player_move(self, row, column):
        if self.board[row][column] == '_':
            self.board[row][column] = self.next_move
            if self.next_move == 'X':
                self.next_move = 'O'
            else:
                self.next_move = 'X'
            return True
        else:
            return False

    # determine who wins the game
    def goal_test(self):
        t_row = self.check_rows('X')
        t_cols = self.check_cols('X')
        t_diag_l = self.check_diag_left('X')
        t_diag_r = self.check_diag_right('X')

        if (t_row or t_cols or t_diag_l or t_diag_r) == True:
            return True,'X'

        o_t_row = self.check_rows('O')
        o_t_cols = self.check_cols('O')
        o_t_diag_l = self.check_diag_left('O')
        o_t_diag_r = self.check_diag_right('O')

        if (o_t_row or o_t_cols or o_t_diag_l or o_t_diag_r) == True:
            return True,'O'

        return False, None

    def find_next_2iar(self, value):
        return_index = []
        value_index = []
        for r in range(5):
            for c in range(6):
                if self.board[r][c] == value:
                    index = r,c
                    value_index.append(index)
        while len(value_index) != 0:
            item = value_index.pop()
            r,c = item
            try:
                # Check row
                if self.board[r][c + 1] == value:
                    if self.board[r][c + 2] == '_':
                        v1 = r
                        v2 = c + 2

                        index = v1,v2
                        return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[r][c - 1] == value:
                    if self.board[r][c - 2] == '_':
                        rr = r
                        rc = c - 2

                        index = rr, rc
                        return_index.append(index)
            except Exception as err:
                err = None
            try:
                # check col
                if self.board[r + 1][c] == value:
                    if self.board[r + 2][c] == '_':
                        rr = r + 2
                        rc = c


                        index = rr, rc
                        return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[r - 1][c] == value:
                    if self.board[r - 2][c] == '_':
                        rr = r - 2
                        rc = c

                        index = rr, rc
                        return_index.append(index)
            except Exception as err:
                err = None
            try:
                # Check diag
                if self.board[r + 1][c + 1] == value:
                    if self.board[r + 2][c + 2] == '_':
                        rr = r + 2
                        rc = c + 2

                        index = rr, rc
                        return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[r + 1][c - 1] == value:
                    if self.board[r + 2][c - 2] == '_':
                        rr = r + 2
                        rc = c - 2

                        index = rr, rc
                        return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[r - 1][c + 1] == value:
                    if self.board[r - 2][c + 2] == '_':
                        rr = r - 2
                        rc = c + 2

                        index = rr, rc
                        return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[r - 1][c - 1] == value:
                    if self.board[r - 2][c - 2] == '_':
                        rr = r - 2
                        rc = c - 2

                        index = rr, rc
                        return_index.append(index)
            except Exception as err:
                err = None
        return return_index


    def find_next_3iar(self, value):
        return_index = []
        value_index = []
        for r in range(5):
            for c in range(6):
                if self.board[r][c] == value:
                    index = r,c
                    value_index.append(index)
        while len(value_index) != 0:
            item = value_index.pop()
            i_r, i_c = item
            try:
                # Check row
                if self.board[i_r][i_c + 1] == value:
                    if self.board[i_r][i_c + 2] == value:
                        if self.board[i_r][i_c + 3] == '_':
                            rr, rc = i_r, i_c + 3

                            index = rr, rc
                            return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[i_r][i_c - 1] == value:
                    if self.board[i_r][i_c - 2] == value:
                        if self.board[i_r][i_c - 3] == '_':
                            rr, rc = i_r, i_c - 3

                            index = rr, rc
                            return_index.append(index)
            except Exception as err:
                err = None
            try:
                # Check col
                if self.board[i_r + 1][i_c] == value:
                    if self.board[i_r + 2][i_c] == value:
                        if self.board[i_r + 3][i_c] == '_':
                            rr, rc = i_r + 3, i_c

                            index = rr, rc
                            return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[i_r - 1][i_c] == value:
                    if self.board[i_r - 2][i_c] == value:
                        if self.board[i_r - 3][i_c] == '_':
                            rr, rc = i_r - 3, i_c

                            index = rr, rc
                            return_index.append(index)
            except Exception as err:
                err = None
            try:
                # Check diag
                if self.board[i_r + 1][i_c + 1] == value:
                    if self.board[i_r + 2][i_c + 2] == value:
                        if self.board[i_r + 3][i_c + 3] == '_':
                            rr, rc = i_r + 3, i_c + 3

                            index = rr,rc
                            return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[i_r - 1][i_c + 1] == value:
                    if self.board[i_r - 2][i_c + 2] == value:
                        if self.board[i_r - 3][i_c + 3] == '_':
                            rr,rc = i_r - 3, i_c + 3

                            index = rr,rc
                            return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[i_r + 1][i_c - 1] == value:
                    if self.board[i_r + 2][i_c - 2] == value:
                        if self.board[i_r + 3][i_c - 3] == '_':
                            rr,rc = i_r + 3, i_c - 3

                            index = rr,rc
                            return_index.append(index)
            except Exception as err:
                err = None
            try:
                if self.board[i_r - 1][i_c - 1] == value:
                    if self.board[i_r - 2][i_c - 2] == value:
                        if self.board[i_r - 3][i_c - 3] == '_':
                            rr,rc=i_r - 3, i_c - 3

                            index = rr,rc
                            return_index.append(index)

            except Exception as err:
                err = None
        return return_index



    def check_diag_left(self, value):
        if self.board[0][3] == value:
            if self.board[1][2] == value:
                if self.board[2][1] == value:
                    if self.board[3][0] == value:
                        return True
        if self.board[0][4] == value:
            if self.board[1][3] == value:
                if self.board[2][2] == value:
                    if self.board[3][1] == value:
                        return True
        if self.board[1][3] == value:
            if self.board[2][2] == value:
                if self.board[3][1] == value:
                    if self.board[4][0] == value:
                        return True
        if self.board[0][5] == value:
            if self.board[1][4] == value:
                if self.board[2][3] == value:
                    if self.board[3][2] == value:
                        return True
        if self.board[1][4] == value:
            if self.board[2][3] == value:
                if self.board[3][2] == value:
                    if self.board[4][1] == value:
                        return True
        if self.board[1][5] == value:
            if self.board[2][4] == value:
                if self.board[3][3] == value:
                    if self.board[4][2] == value:
                        return True
        return False


    def check_diag_right(self, value):
        if self.board[1][0] == value:
            if self.board[2][1] == value:
                if self.board[3][2] == value:
                    if self.board[4][3] == value:
                        return True
        if self.board[0][0] == value:
            if self.board[1][1] == value:
                if self.board[2][2] == value:
                    if self.board[3][3] == value:
                        return True
        if self.board[1][1] == value:
            if self.board[2][2] == value:
                if self.board[3][3] == value:
                    if self.board[4][4] == value:
                        return True
        if self.board[0][1] == value:
            if self.board[1][2] == value:
                if self.board[2][3] == value:
                    if self.board[3][4] == value:
                        return True
        if self.board[1][2] == value:
            if self.board[2][3] == value:
                if self.board[3][4] == value:
                    if self.board[4][5] == value:
                        return True
        if self.board[0][2] == value:
            if self.board[1][3] == value:
                if self.board[2][4] == value:
                    if self.board[3][5] == value:
                        return True
        return False

    def check_cols(self, value):
        for col in range(6):
            if self.board[0][col] == value:
                if self.board[1][col] == value:
                    if self.board[2][col] == value:
                        if self.board[3][col] == value:
                            return True
            if self.board[1][col] == value:
                if self.board[2][col] == value:
                    if self.board[3][col] == value:
                        if self.board[4][col] == value:
                            return True
        return False


    def check_rows(self, value):
        for row in range(5):
            if self.board[row][0] == value:
                if self.board[row][1] == value:
                    if self.board[row][2] == value:
                        if self.board[row][3] == value:
                            return True
            if self.board[row][1] == value:
                if self.board[row][2] == value:
                    if self.board[row][3] == value:
                        if self.board[row][4] == value:
                            return True
            if self.board[row][2] == value:
                if self.board[row][3] == value:
                    if self.board[row][4] == value:
                        if self.board[row][5] == value:
                            return True
        return False








    def print_board(self):
        print '  0 1 2 3 4 5'
        for row in range(5):
            print row, self.board[row][0], self.board[row][1], self.board[row][2], self.board[row][3], self.board[row][4], self.board[row][5]
        #print
        print 'Next turn -> ', self.next_move
        print
