class two_in_a_row():
    def __init__(self, first_i, second_i, open_i):
        self.first = first_i
        self.second = second_i
        self.open = open_i

    def print_2iar(self):
        print '1-> ', self.first, ' 2-> ', self.second
        print 'open -> ', self.open

    def is_in(self, item):
        first = self.first
        second = self.second
        if item == (first or second):
            return True
        else:
            return False

class three_in_a_row():

    def __init__(self, first_i, second_i, third_i, open_i):
        self.first = first_i
        self.second = second_i
        self.third = third_i
        self.open = open_i


    def print_3iar(self):
        print '1-> ', self.first, ' 2-> ', self.second, ' 3-> ', self.third
        print 'open -> ', self.open

    def get_open_as_index(self):
        r,c = self.open
        return r,c



    def is_in(self, item):
        first = self.first
        second = self.second
        third = self.third
        if item == (first or second or third):
            return True
        else:
            return False



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

        print '<--------->'
        print '<- h ->', h
        print '<--------->'

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
        r_mx = 4
        r_mi = 0
        c_mx = 5
        c_mi = 0
        list_2iar = []
        value_index = []
        for r in range(5):
            for c in range(6):
                if self.board[r][c] == value:
                    index = r,c
                    value_index.append(index)
        for item in value_index:
            for index in list_2iar:
                result = index.is_in(item)
                if result:
                    print 'Already in 2 in a row'
                    continue
            r,c = item

            # Check row+ for 2iar
            test_r, test_c = r,c
            first = None
            second = None
            final = None
            while(r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r,test_c
                    elif second == None:
                        second = test_r,test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second != None:
                        final = test_r,test_c
                        new_2iar = two_in_a_row(first, second, final)
                        list_2iar.append(new_2iar)
                        break
                    else:
                        break
                else:
                    break
                test_c += 1

            # Check row- for 2iar
            test_r, test_c = r, c
            first = None
            second = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second != None:
                        final = test_r, test_c
                        new_2iar = two_in_a_row(first, second, final)
                        list_2iar.append(new_2iar)
                        break
                    else:
                        break
                else:
                    break
                test_c -= 1

            # Check col+ for 2iar
            test_r, test_c = r, c
            first = None
            second = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second != None:
                        final = test_r, test_c
                        new_2iar = two_in_a_row(first, second, final)
                        list_2iar.append(new_2iar)
                        break
                    else:
                        break
                else:
                    break
                test_r += 1

            # Check col- for 2iar
            test_r, test_c = r, c
            first = None
            second = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second != None:
                        final = test_r, test_c
                        new_2iar = two_in_a_row(first, second, final)
                        list_2iar.append(new_2iar)
                        break
                    else:
                        break
                else:
                    break
                test_r -= 1

            # Check diag++ for 2iar
            test_r, test_c = r, c
            first = None
            second = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second != None:
                        final = test_r, test_c
                        new_2iar = two_in_a_row(first, second, final)
                        list_2iar.append(new_2iar)
                        break
                    else:
                        break
                else:
                    break
                test_r += 1
                test_c += 1

            # Check diag+- for 2iar
            test_r, test_c = r, c
            first = None
            second = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second != None:
                        final = test_r, test_c
                        new_2iar = two_in_a_row(first, second, final)
                        list_2iar.append(new_2iar)
                        break
                    else:
                        break
                else:
                    break
                test_r += 1
                test_c -= 1

            # Check diag-+ for 2iar
            test_r, test_c = r, c
            first = None
            second = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second != None:
                        final = test_r, test_c
                        new_2iar = two_in_a_row(first, second, final)
                        list_2iar.append(new_2iar)
                        break
                    else:
                        break
                else:
                    break
                test_r -= 1
                test_c += 1

            # Check diag-- for 2iar
            test_r, test_c = r, c
            first = None
            second = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second != None:
                        final = test_r, test_c
                        new_2iar = two_in_a_row(first, second, final)
                        list_2iar.append(new_2iar)
                        break
                    else:
                        break
                else:
                    break
                test_r -= 1
                test_c -= 1

        return list_2iar


    def find_next_3iar(self, value):
        r_mx = 4
        r_mi = 0
        c_mx = 5
        c_mi = 0
        list_3iar = []
        value_index = []
        for r in range(5):
            for c in range(6):
                if self.board[r][c] == value:
                    index = r,c
                    value_index.append(index)
        for item in value_index:

            #item = value_index.pop()
            for index in list_3iar:
                result = index.is_in(item)
                if result:
                    print "Already in 3 in a row"
                    continue
            i_r, i_c = item


            #check row+ for 3iar
            test_r, test_c = i_r, i_c
            first = None
            second = None
            third = None
            final = None
            while(r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx ):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r,test_c
                    elif second == None:
                        second = test_r, test_c
                    elif third == None:
                        third = test_r,test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second and third != None:
                        final = test_r, test_c
                        new_3iar = three_in_a_row(first, second, third, final)
                        list_3iar.append(new_3iar)
                        break
                    else:
                        break
                else:
                    break

                test_c += 1

            # check row- for 3iar
            test_r, test_c = i_r, i_c
            first = None
            second = None
            third = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    elif third == None:
                        third = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second and third != None:
                        final = test_r, test_c
                        new_3iar = three_in_a_row(first, second, third, final)
                        list_3iar.append(new_3iar)
                        break
                    else:
                        break
                else:
                    break

                test_c -= 1

            # check col+ for 3iar
            test_r, test_c = i_r, i_c
            first = None
            second = None
            third = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    elif third == None:
                        third = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second and third != None:
                        final = test_r, test_c
                        new_3iar = three_in_a_row(first, second, third, final)
                        list_3iar.append(new_3iar)
                        break
                    else:
                        break
                else:
                    break

                test_r += 1

            # check col- for 3iar
            test_r, test_c = i_r, i_c
            first = None
            second = None
            third = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    elif third == None:
                        third = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second and third != None:
                        final = test_r, test_c
                        new_3iar = three_in_a_row(first, second, third, final)
                        list_3iar.append(new_3iar)
                        break
                    else:
                        break
                else:
                    break

                test_r -= 1

            # check diag++ for 3iar
            test_r, test_c = i_r, i_c
            first = None
            second = None
            third = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    elif third == None:
                        third = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second and third != None:
                        final = test_r, test_c
                        new_3iar = three_in_a_row(first, second, third, final)
                        list_3iar.append(new_3iar)
                        break
                    else:
                        break
                else:
                    break

                test_c += 1
                test_r += 1

            # check diag+- for 3iar
            test_r, test_c = i_r, i_c
            first = None
            second = None
            third = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    elif third == None:
                        third = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second and third != None:
                        final = test_r, test_c
                        new_3iar = three_in_a_row(first, second, third, final)
                        list_3iar.append(new_3iar)
                        break
                    else:
                        break
                else:
                    break
                test_r += 1
                test_c -= 1

            # check diag-+ for 3iar
            test_r, test_c = i_r, i_c
            first = None
            second = None
            third = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    elif third == None:
                        third = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second and third != None:
                        final = test_r, test_c
                        new_3iar = three_in_a_row(first, second, third, final)
                        list_3iar.append(new_3iar)
                        break
                    else:
                        break
                else:
                    break
                test_r -= 1
                test_c += 1

            # check diag-- for 3iar
            test_r, test_c = i_r, i_c
            first = None
            second = None
            third = None
            final = None
            while (r_mi <= test_r <= r_mx and c_mi <= test_c <= c_mx):
                if self.board[test_r][test_c] == value:
                    if first == None:
                        first = test_r, test_c
                    elif second == None:
                        second = test_r, test_c
                    elif third == None:
                        third = test_r, test_c
                    else:
                        break
                elif self.board[test_r][test_c] == '_':
                    if first and second and third != None:
                        final = test_r, test_c
                        new_3iar = three_in_a_row(first, second, third, final)
                        list_3iar.append(new_3iar)
                        break
                    else:
                        break
                else:
                    break
                test_r -= 1
                test_c -= 1




        return list_3iar


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
