from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/mills')
def hello(name=None):
    return render_template('main.html', name=name)

@app.route('/play')
def play(): pass

@app.route('/rules')
def rules(): pass

@app.route('/ranking')
def ranking(): pass

if __name__ == '__main__':
    app.run()
