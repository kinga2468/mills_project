from player import Player
#from game import Game

class Board:
    def __init__(self):
        # self.fields = {      #pola mogą być 'F', '*', '@'
        #     0 :'F',
        #     1: 'F',
        #     2: 'F',
        #     3: 'F',
        #     4: 'F',
        #     5: 'F',
        #     6: 'F',
        #     7: 'F',
        #     8: 'F',
        #     9: 'F',
        #     10: 'F',
        #     11: 'F',
        #     12: 'F',
        #     13: 'F',
        #     14: 'F',
        #     15: 'F',
        #     16: 'F',
        #     17: 'F',
        #     18: 'F',
        #     19: 'F',
        #     20: 'F',
        #     21: 'F',
        #     22: 'F',
        #     23: 'F',
        # }

        # pola mogą być 'F', '*', '@'
        self.fields = ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
                       'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']

        self.neighbors = {
            0: [1, 9],
            1: [0, 2, 4],
            2: [1, 14],
            3: [4, 10],
            4: [1, 3, 5, 7],
            5: [4, 13],
            6: [7, 11],
            7: [4, 6, 8],
            8: [7, 12],
            9: [0, 10, 21],
            10: [3, 9, 11, 18],
            11: [6, 10, 15],
            12: [8, 13, 17],
            13: [5, 12, 14, 20],
            14: [2, 13, 23],
            15: [11, 16],
            16: [15, 17, 19],
            17: [12, 16],
            18: [10, 19],
            19: [16, 18, 20, 22],
            20: [13, 19],
            21: [9, 22],
            22: [19, 21, 23],
            23: [14, 22]
        }

    def take_the_field(self, color, field_to, game):
        if self.is_field_empty(field_to):
            self.fields[field_to] = game.current_player.color
            game.current_player.pawns.player_pawns[self.player_pawns_on_board(game) - 1] = 'on_board'
            return True
        else:
            return False
            # zmiana w player_pawn statusu na 'on_board'
            # Player.pawns.player_pawns[field_to] = 'on_board'


    def is_field_empty(self, field_to):
        if self.fields[field_to] == 'F':
            return True
            # self.take_the_field(color, field_to)
        else:
            return False


    def take_enemy_pawn(self, field_to, game):
        if self.is_field_enemys(field_to, game):
            self.fields[field_to] = 'F'
            game.pawns.player_pawns[self.player_pawns_on_board(game) - 1] = 'lost'
            return True
        else:
            return False


    def is_field_enemys(self, remove_field, game):
        if self.fields[remove_field] == game.current_player.color:
            return True
        else:
            return False

    def player_pawns_on_board(self, game):
        counter = 0
        for i in self.fields:
            if i == game.current_player.color:
                counter = counter + 1
        return counter

    def have_mills(self, field_to, game):
        color = game.current_player.color
        if self.fields[field_to] == self.fields[0] and ((self.fields[1] == color and self.fields[2] == color) or (self.fields[9] == color and self.fields[21] == color)):
            print("zabierz pionek przeciwnka1")
            return True
        if self.fields[field_to] == self.fields[1] and ((self.fields[0] == color and self.fields[2] == color) or (self.fields[4] == color and self.fields[7] == color)):
            print("zabierz pionek przeciwnka2")
            return True
        if self.fields[field_to] == self.fields[2] and ((self.fields[0] == color and self.fields[1] == color) or (self.fields[14] == color and self.fields[23] == color)):
            print("zabierz pionek przeciwnka3")
            return True
        if self.fields[field_to] == self.fields[3] and ((self.fields[4] == color and self.fields[5] == color) or (self.fields[10] == color and self.fields[18] == color)):
            print("zabierz pionek przeciwnka4")
            return True
        if self.fields[field_to] == self.fields[4] and ((self.fields[3] == color and self.fields[5] == color) or (self.fields[1] == color and self.fields[7] == color)):
            print("zabierz pionek przeciwnka5")
            return True
        if self.fields[field_to] == self.fields[5] and ((self.fields[3] == color and self.fields[4] == color) or (self.fields[13] == color and self.fields[20] == color)):
            print("zabierz pionek przeciwnka6")
            return True
        if self.fields[field_to] == self.fields[6] and ((self.fields[7] == color and self.fields[8] == color) or (self.fields[11] == color and self.fields[19] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[7] and ((self.fields[6] == color and self.fields[8] == color) or (self.fields[1] == color and self.fields[4] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[8] and ((self.fields[6] == color and self.fields[7] == color) or (self.fields[12] == color and self.fields[17] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[9] and ((self.fields[10] == color and self.fields[11] == color) or (self.fields[0] == color and self.fields[21] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[10] and ((self.fields[11] == color and self.fields[9] == color) or (self.fields[3] == color and self.fields[18] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[11] and ((self.fields[6] == color and self.fields[15] == color) or (self.fields[9] == color and self.fields[10] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[12] and ((self.fields[13] == color and self.fields[14] == color) or (self.fields[8] == color and self.fields[17] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[13] and ((self.fields[12] == color and self.fields[14] == color) or (self.fields[5] == color and self.fields[20] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[14] and ((self.fields[2] == color and self.fields[23] == color) or (self.fields[12] == color and self.fields[13] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[15] and ((self.fields[6] == color and self.fields[11] == color) or (self.fields[16] == color and self.fields[17] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[16] and ((self.fields[15] == color and self.fields[17] == color) or (self.fields[19] == color and self.fields[22] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[17] and ((self.fields[8] == color and self.fields[12] == color) or (self.fields[15] == color and self.fields[16] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[18] and ((self.fields[19] == color and self.fields[20] == color) or (self.fields[3] == color and self.fields[10] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[19] and ((self.fields[18] == color and self.fields[20] == color) or (self.fields[16] == color and self.fields[22] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[20] and ((self.fields[18] == color and self.fields[19] == color) or (self.fields[5] == color and self.fields[13] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[21] and ((self.fields[0] == color and self.fields[9] == color) or (self.fields[22] == color and self.fields[23] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[22] and ((self.fields[21] == color and self.fields[23] == color) or (self.fields[16] == color and self.fields[19] == color)):
            print("zabierz pionek przeciwnka")
            return True
        if self.fields[field_to] == self.fields[23] and ((self.fields[21] == color and self.fields[22] == color) or (self.fields[2] == color and self.fields[14] == color)):
            print("zabierz pionek przeciwnka")
            return True

        # if self.fields[0] == color and self.fields[1] == color and self.fields[2] == color:
        #     # self.take_enemy_pawn(color, field_to, game)
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[3] == color and self.fields[4] == color and self.fields[5] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[6] == color and self.fields[7] == color and self.fields[8] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[9] == color and self.fields[10] == color and self.fields[11] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[12] == color and self.fields[13] == color and self.fields[14] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[15] == color and self.fields[16] == color and self.fields[17] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[18] == color and self.fields[19] == color and self.fields[20] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[21] == color and self.fields[22] == color and self.fields[23] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[0] == color and self.fields[9] == color and self.fields[21] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[3] == color and self.fields[10] == color and self.fields[18] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[6] == color and self.fields[11] == color and self.fields[15] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[1] == color and self.fields[4] == color and self.fields[7] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[16] == color and self.fields[19] == color and self.fields[22] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[8] == color and self.fields[12] == color and self.fields[17] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[5] == color and self.fields[13] == color and self.fields[20] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # if self.fields[2] == color and self.fields[14] == color and self.fields[23] == color:
        #     print("zabierz pionek przeciwnka")
        #     return True
        # else:
        #     return False

    def move(self, field_from, field_to, game):
        if field_to in self.field_to_possible(field_from):
            self.fields[field_from] = 'F'
            self.fields[field_to] = game.current_player.color
            print("ruch został wykonany")
            return True
        else:
            return False

    def field_to_possible(self, field_from):
        return self.neighbors[field_from]


    def if_pawn_to_move_is_yours(self, field_from, game):
        if self.fields[field_from] == game.current_player.color:
            return True
        else:
            return False