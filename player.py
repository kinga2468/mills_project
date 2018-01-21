from board import Board
from game import Game

class Player():
    """klasa defuniująca graczy"""

    def __init__(self, sign):
        self.sign = sign
        # self.name = name
        # self.color = color

    def take_the_field(self, sign, field_to):
        board.fields[field_to] = game.current_player.sign
        # Pawns.amount = Pawns.amount - 1

    def sign(self):
        return self.sign




