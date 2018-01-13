class Board:
    def __init__(self):
        self.field = {}
        for i in range(23):
            nr = i +1
            self.field[nr] = 'F'   #pola mogą być 'F', 'P', 'E'

    def is_field_empty(self, field_to):
        if (field_to == 'F'):
            return True
        else:
            return False























