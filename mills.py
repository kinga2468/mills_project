from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/proba')
def proba():
    return render_template('proba.html')

if __name__ == '__main__':
    app.run()
