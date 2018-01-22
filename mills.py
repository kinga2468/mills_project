from flask import Flask, render_template, jsonify, request, session
from game import Game

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('MILLS_SETTINGS', silent=True)


@app.route('/mills')
def start():
    # session.clear()
    return render_template('main.html')

@app.route('/play')
def play():
    global game
    game = Game()

    current_player = game.current_player
    board = game.board
    # pawns = game.pawns.amount
    return render_template('new_board.html', current_player = current_player, board = board )

# @app.route('/add/<nr>')
# def add(nr):
#     nr = {'nr': int(nr)}
#
#     game.board.take_the_field(game.current_player.color, nr)
#     game.change_player()
#     current_player = game.current_player
#     board = game.board
#
#     return render_template('new_board.html', current_player = current_player, board = board)

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 24, type=int)
    game.board.take_the_field(game.current_player.color, a)
    # game.change_player()
    # current_player = game.current_player
    # board = game.board

    return jsonify(result = game.current_player.color)


# @app.route('/background_process')
# def background_process():
#     try:
#         lang = request.args.get('move_to', 0, type=str)
#         if lang.lower() == 'python':
#             print("you are wise")
#             # return jsonify(result='You are wise')
#         else:
#             # return jsonify(result='Try again.')
#             print("or not")
#     except Exception as e:
#         return str(e)

@app.route('/rules')
def rules(): pass
    #return render_template('board.html')

@app.route('/ranking')
def ranking(): pass

if __name__ == '__main__':
    app.debug = True
    # port = 5003
    app.run()


