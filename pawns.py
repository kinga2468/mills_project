from board import Board
class Pawns():
    """klasa defuniująca pionki oraz ich funkcje"""

    def __init__(self, color, amount, status):
        self.color = color
        self.amount = 9
        self.status = 'free'  #statusy pionków : free, on_board, lost

    #def status_checking(self, status):
    #    """ """
    #    pass

    #if (self.status == 'free'):
    def adding_pawns(self, field_to):
        """1 faza gry, stawianie pionków na planszy"""
        if (Board.is_field_empty(field_to)) :
            pass
