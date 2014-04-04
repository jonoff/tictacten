#!/usr/bin/env python
import random
import time

import AI
from board import board, big_board, move, marks, BLANK

class game(object):
    def __init__(self, p1, p2):
        self.board = big_board()
        self.mini = board()
        self.turn = 1
        self.current_player = None
        self.p1 = p1
        self.p1.set_mark(marks[0])
        self.p2 = p2
        self.p2.set_mark(marks[1])
        self.marks = {self.p1: marks[0], self.p2: marks[1]}
        self.gameover = False
        self.last_move = move()

    def mark(self, sb):
        sb[self.last_move.x][self.last_move.y] = self.marks[self.current_player]
        return

    def start_game(self, delay=0):
        def toggle():
            if self.current_player == self.p1:
                return self.p2
            return self.p1

        self.current_player = random.choice((self.p1, self.p2))
        #import pdb; pdb.set_trace()
        while not self.gameover:
            self.move(self.current_player)
            self.current_player = toggle()
            time.sleep(delay)
        self.end_game()

    def end_game(self):
        print "Game over, winner: %s" % self.winner

    def move(self, p):
        self.last_move = p.move(self.board, self.last_move.x, self.last_move.y)
        x, y = self.last_move.x, self.last_move.y
        bx, by = self.last_move.boardx, self.last_move.boardy
        self.mini[x][y] = '.'
        self.mark(self.board[bx][by])

        print 'TURN: %d' % self.turn
        print self.board
        print '\nNext move:\n%s' % self.mini
        print '\n\n'

        #check win
        if self.check_win() != BLANK:
            print self.check_win()
            self.gameover = True
            self.winner = self.check_win()
        self.turn += 1
        self.mini.clear()

    def check_win(self):
        return self.board.check_win()


bb = big_board()
bb.randomize()
#bb.check_win()
#print bb

g = game(AI.random_bot(), AI.center_bot())
g.start_game(delay=0.1)
