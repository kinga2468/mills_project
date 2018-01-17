class Pawns():
    """klasa defuniująca pionki oraz ich funkcje"""

    def __init__(self):
        self.amount = 9
        self.status = 'free'  #statusy pionków : free, on_board, lost

    # def show_free_pawns(self, status):
    #     """wyświetla pionki do ustawienia poza planszą"""
    #     if self.status == 'free':
    #         pass
    #
    #
    # #if (self.status == 'free'):
    # def adding_pawns(self, field_to):
    #     """1 faza gry, stawianie pionków na planszy"""
    #     if (Board.is_field_empty(field_to) :
    #         pass
