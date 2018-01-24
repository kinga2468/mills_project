class Pawns():
    """klasa defuniująca pionki oraz ich funkcje"""

    def __init__(self):
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

