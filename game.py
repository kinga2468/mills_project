from board import Board
from player import Player
import random
from pawns import Pawns

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('green')
        self.player2 = Player('pink')
        self.current_player = random.choice([self.player1, self.player2])
        # self.nr = nr
        # self.pawns = Pawns()

    def change_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1













