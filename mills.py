from flask import Flask, render_template, jsonify, request,  redirect, url_for
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
    # current_color = game.current_player.color
    print("ilość pionków playera na plaszy przed ruchem ", game.board.player_pawns_on_board(game))
    print("czy prawdą jest że mam wolny pionek: ",game.pawns.if_is_free_pawn(game))
    print("statusy pionków przed ruchem ", game.current_player.pawns.player_pawns)
    if (game.board.player_pawns_on_board(game) <= 9 and game.current_player.pawns.if_is_free_pawn(game) is True):
        a = request.args.get('a', 24, type=int)
        #jeśli pionków gracza na plaszy jest mniej niż 9 to dostawiaj pionki
        if game.board.take_the_field(game.current_player.color, a, game) is True:
            #jeśli udało się zająć pole (nie było ono już wcześniej zajęte)
            print("ilość pionków playera na plaszy po ruchu", game.board.player_pawns_on_board(game))
            print("statusy pionków po ruchu ", game.current_player.pawns.player_pawns)
            print("plansza wygląda tak1 ", game.board.fields)
            # if game.board.take_enemy_pawn(game.current_player.color, b, game):
            #     print("udało ci się zabrać pionek przeciwnika")
            # else:
            #     print("nie udało ci sie zabrać pionka przeciwnika")




            if game.board.have_mills(a, game) == True:
                # b = request.args.get('b', 24, type=int)
                # game.board.take_enemy_pawn(b, game)
                print("zabrałam pionek przeciwnika")
                # return redirect(url_for('remove'))
                # return True
            else:
                print("nie możesz zabrać pionka przeciwnka")
                # return False

            current_color = game.current_player.color
            game.change_player()
        else:
            # current_color = game.current_player.color
            print("to pole jest już zajęte, wybierz inne")
            # return False
    elif (game.board.player_pawns_on_board(game) > 3 and game.current_player.pawns.if_is_free_pawn(game) is False):
        c = request.args.get('c', 24, type=int)
        d = request.args.get('d', 24, type=int)
        if (game.board.if_pawn_to_move_is_yours(c, game) and game.board.is_field_empty(d)):
            game.board.move(c, d, game)
            print("wykonałem ruch z pola :", c,"na pole :", d)
            current_color = game.current_player.color
            game.change_player()
        else:
            print("nie można wykonać tego ruchu ")

        # print("moje możliwe ruchy to :", game.board.field_to_possible(8))
    else:
        print("nie masz więcej pionków")
        # return False


        # current_player = game.current_player
    # print("zajął pole ", a)
    print("teraz będzie grał ", game.current_player.color)
    print("plansza wygląda tak3 ", game.board.fields)

    # board = game.board

    return jsonify(result = game.second_player.color, second_player = current_color)

@app.route('/remove')
def remove():
    b = request.args.get('b', 24, type=int)
    game.board.take_enemy_pawn(b, game)



@app.route('/rules')
def rules(): pass
    #return render_template('board.html')

@app.route('/ranking')
def ranking(): pass

if __name__ == '__main__':
    app.debug = True
    # port = 5003
    app.run()


