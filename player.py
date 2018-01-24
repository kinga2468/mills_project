from pawns import Pawns

class Player():
    """klasa defuniująca graczy"""

    def __init__(self, color):
        self.color = color
        self.pawns = Pawns()
        # self.name = name


    def color(self):
        return self.color



