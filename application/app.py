from random import choice
from flask import Flask
app = Flask(__name__)

def pick_greeting():
    return choice(["Greetings", "Hello", "Hey"])

@app.route('/')
def hello_world():
    return '{greeting} World!'.format(greeting=pick_greeting())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
