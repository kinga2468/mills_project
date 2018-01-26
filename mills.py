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
    print("zaczyna: ", game.current_player.color)
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

@app.route('/add')
def add():
    a = request.args.get('a', 24, type=int)
    b = request.args.get('b', 24, type = int)
    print("ilość pionków playera na plaszy przed ruchem ", game.board.player_pawns_on_board(game))
    print("czy prawdą jest że mam wolny pionek: ",game.pawns.if_is_free_pawn())
    print("statusy pionków przed ruchem ", game.current_player.pawns.player_pawns)
    if (game.board.player_pawns_on_board(game) <= 9 and game.current_player.pawns.if_is_free_pawn() is True):
        #jeśli pionków gracza na plaszy jest mniej niż 9 to dostawiaj pionki
        # game.pawns.player_pawns[game.board.player_pawns_on_board(game)] = 'on_board'
        if game.board.take_the_field(game.current_player.color, a, game) is True:
            #jeśli udało się zająć pole (nie było ono już wcześniej zajęte)
            print("ilość pionków playera na plaszy po ruchu", game.board.player_pawns_on_board(game))
            print("statusy pionków po ruchu ", game.current_player.pawns.player_pawns)

            # if game.board.take_enemy_pawn(game.current_player.color, b, game):
            #     print("udało ci się zabrać pionek przeciwnika")
            # else:
            #     print("nie udało ci sie zabrać pionka przeciwnika")




            if game.board.have_mills(a, game) == True:
                print("zabrałam pionek przeciwnika")
                # return True
            else:
                print("nie możesz zabrać pionka przeciwnka")
                # return False

            # current_color = game.current_player.color
            game.change_player()
        else:
            # current_color = game.current_player.color
            print("to pole jest już zajęte, wybierz inne")
            # return False
    else:
        print("nie masz więcej pionków")
        # return False


        # current_player = game.current_player
    print("zajął pole ", a)
    print("teraz będzie grał ", game.current_player.color)
    print("plansza wygląda tak ", game.board.fields)

    # board = game.board

    return jsonify(result = game.second_player.color)


@app.route('/rules')
def rules(): pass
    #return render_template('board.html')

@app.route('/ranking')
def ranking(): pass

if __name__ == '__main__':
    app.debug = True
    # port = 5003
    app.run()


