#Написать функцию, которая будет принимать на вход строку и
#выводить на экран ее длину.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/len/<text>/')
def get_len(text):
    return f'Длина строки {text} = {len(text)}' 


if __name__ == '__main__':
    app.run(debug=True)