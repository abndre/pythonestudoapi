from flask import Flask, escape, request
from flask_restplus import abort

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/breakfunc')
def breakfunc():
    dead()

def dead():
    abort(403, message="hAAAAAAAAAAAAAAA")

@app.route('/calc/<int:n_prim>')
def cal_prim(n_prim):
    return "Prim {}".format(n_prim)

if __name__ == "__main__":
    app.run(debug=True)