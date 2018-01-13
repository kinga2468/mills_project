from flask import Flask
from flask import render_template
from move import *
from board import *

app = Flask(__name__)

@app.route('/mills')
def start():
    return render_template('main.html')

@app.route('/play')
def play():
    return render_template('board.html')

@app.route('/rules')
def rules(): pass
    #return render_template('board.html')

@app.route('/ranking')
def ranking(): pass

if __name__ == '__main__':
    app.run()
