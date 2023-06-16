from flask import Flask,jsonify
from assignment_2 import out
from hello import *

app = Flask(__name__)

@app.route('/api/printHello')
def print():
    return call_me()

@app.route('/api/modifyRecepie')
def hi():
    data=out()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)