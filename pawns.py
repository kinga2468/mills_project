class Pawns():
    """klasa defuniująca pionki oraz ich funkcje"""

    def __init__(self):
        # self.amount = 9
        # self.status = 'free'  #statusy pionków : free, on_board, lost

        self.player_pawns = ['free', 'free', 'free', 'free', 'free', 'free', 'free', 'free', 'free']
        self.free = []

    def is_pawn_free(self, pawn_nr):
        if pawn_nr == 'free':
            return True
        else:
            return False

    def how_many_free_pawns(self):
        for x in self.player_pawns:
            if x == 'free':
                self.free.append(x)
        return len(self.free)

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
