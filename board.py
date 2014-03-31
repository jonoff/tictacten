# -*- coding: UTF-8 -*-
import random
BLANK = '_'
marks = ('X', 'O')

class move(object):
    def __init__(self, x=None, y=None, boardx=None, boardy=None):
        self.boardx = boardx
        self.boardy = boardy
        self.x = x
        self.y = y

class board(object):
    def __init__(self):
        self.squares = [[BLANK for i in xrange(3)] for i in xrange(3)]
        self.winner = BLANK

    def __repr__(self):
        return '\n'.join(self.display())

    def __getitem__(self, key):
        return self.squares[key]

    def randomize(self):
        for x in range(3):
            for y in range(3):
                self.squares[x][y] = random.choice(marks)

    def clear(self):
        for x in range(3):
            for y in range(3):
                self.squares[x][y] = BLANK

    def open_pos(self):
        pos = []
        for x in range(3):
            for y in range(3):
                if self.squares[x][y] == BLANK:
                    pos.append((x,y))
        return pos

    def display(self, suffix='\n'):
        winner = self.check_win()
        if winner == marks[0]:
            return [' \ / ', '  X  ', ' / \ ']
        elif winner == marks[1]:
            return ['  _  ', ' | | ', '  ‾  ']
        elif winner == 'C':
            return ['  __ ', '  |  ', '  ‾‾ ']

        rows = []
        for row in self.squares:
            rows.append('|'.join(row))
        return rows

    def check_win(self):
        #TODO blank vs none
        if self.winner != BLANK:
            return self.winner

        # check horz
        for row in self.squares:
            if set(row) != set(BLANK) and len(set(row)) == 1:
                self.winner = row[0]
                return self.winner

        # check vert
        for i in range(3):
            col = [x[i] for x in self.squares]
            if set(col) != set(BLANK) and len(set(col)) == 1:
                self.winner = col[0]
                return self.winner

        # check diag
        diag = (self.squares[0][0], self.squares[1][1], self.squares[2][2])
        if set(diag) != set(BLANK) and len(set(diag)) == 1:
            self.winner = diag[0]
            return self.winner
        diag = (self.squares[0][2], self.squares[1][1], self.squares[2][0])
        if set(diag) != set(BLANK) and len(set(diag)) == 1:
            self.winner = diag[0]
            return self.winner

        #cats game
        s = [(x,y) for x in range(3) for y in range(3)]
        for x in range(3):
            for y in range(3):
                if self.squares[x][y] != BLANK:
                    s.remove((x,y))
        if not s:
            self.winner = 'C'
            return self.winner

        return BLANK


class big_board(object):
    def __init__(self):
        self.squares = [[board() for i in xrange(3)] for i in xrange(3)]

    def __repr__(self):
        return '\n'.join(self.display())

    def __getitem__(self, key):
        return self.squares[key]

    def display(self):
        ret = []
        for row in self.squares:
            r = [x.display() for x in row]
            for i in range(len(row)):
                ret.append(' | '.join([x[i] for x in r]))
            if row != self.squares[-1]:
                ret.append('-'*(7*3))
        return ret

    def randomize(self):
        for x in self.squares:
            for y in x:
                y.randomize()

    def open_boards(self):
        boards = []
        for x in range(3):
            for y in range(3):
                if self.squares[x][y].check_win() == BLANK:
                    boards.append((x,y))
        return boards

    def check_win(self):
        #import pdb; pdb.set_trace()
        # check horz and vert
        for i in range(3):
            row = [x.check_win() for x in self.squares[i]]
            if all(row) and len(set(row)) == 1:
                return row[0]

            col = [x[i].check_win() for x in self.squares]
            if all(col) and len(set(col)) == 1:
                return col[0]

        # check diag
        diag = (self.squares[0][0].check_win(), self.squares[1][1].check_win(), self.squares[2][2].check_win())
        if all(diag) and len(set(diag)) == 1:
            return diag[0]
        diag = (self.squares[0][2].check_win(), self.squares[1][1].check_win(), self.squares[2][0].check_win())
        if all(diag) and len(set(diag)) == 1:
            return diag[0]

        s = [(x,y) for x in range(3) for y in range(3)]
        for x in range(3):
            for y in range(3):
                if self.squares[x][y].check_win() != BLANK:
                    s.remove((x,y))
        if not s:
            return 'C'

        return BLANK
