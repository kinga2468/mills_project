from flask import Flask, render_template
from game import Game

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MILLS_SETTINGS', silent=True)


@app.route('/mills')
def start():
    return render_template('main.html')

@app.route('/play')
def play():
    global game
    game = Game()
    current_player = game.current_player
    board = game.board
    # pawns = game.pawns.amount
    return render_template('new_board.html', current_player = current_player, board = board )

# @app.route('/add/<field_to>')
# def add(field_to):
#     field_to = {'field_to': int(field_to)}
#
#     game.board.take_the_field(game.current_player.sign, field_to)
#     game.change_player()
#     current_player = game.current_player
#     board = game.board
#
#     return render_template('new_board.html', current_player = current_player, board = board)

@app.route('/rules')
def rules(): pass
    #return render_template('board.html')

@app.route('/ranking')
def ranking(): pass

if __name__ == '__main__':
    app.debug = True
    # port = 5003
    app.run()


