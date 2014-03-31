#!/usr/bin/env python
import random
from board import board, BLANK, move

class random_bot(object):
    ''' Bot that randomly chooses a valid move '''
    def set_mark(self, mark):
        self.mark = mark
        self.bb = None

    def move(self, bb, x,y):
        self.bb = bb
        boards = self.bb.open_boards()
        random.shuffle(boards)
        if x == None:
            x,y = boards.pop()

        while self.bb[x][y].check_win() != BLANK:
            x,y = boards.pop()

        ps = self.bb[x][y].open_pos()
        random.shuffle(ps)
        px,py = ps.pop()
        print 'board(%d,%d) pos:(%d,%d)' % (x,y,px,py)
        return move(px, py, boardx=x, boardy=y)

class return_bot(random_bot):
    ''' Bot that sends player back to the board they came from '''
    pass

class centerBot(random_bot):
    ''' Bot that always chooses the center option if available '''
    def move(self, board, bb):
        if board[1][1] == BLANK:
            return move(1,1)
        else:
            return random_bot().move(board, bb)

class greedyBot(random_bot):
    pass


