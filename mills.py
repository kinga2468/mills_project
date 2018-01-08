from flask import Flask
from flask import render_template
from move import *
from board import *

app = Flask(__name__)

@app.route('/mills')
def start():
    return render_template('main.html')

@app.route('/start')
def start(): pass

# @app.route('/play', methods=['GET', 'POST'])
# def play():
#     plansza = Board.()
#     zmiany = 0
#     for key in request.form:
#         stara = plansza.t[key]
#         nowa = int(request.form[key])
#         if stara != nowa:
#             zmiany += 1
#             plansza.t[key] = request.form[key]
#     f = open('zapis.txt', 'w+')
#     f.write(str(plansza()))
#     f.close()
#     # return str(plansza())
#     return render_template('plansza.htm', p=plansza(), zmiany=zmiany)


@app.route('/rules')
def rules(): pass

@app.route('/ranking')
def ranking(): pass

if __name__ == '__main__':
    app.run()
