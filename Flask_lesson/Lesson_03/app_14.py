from flask import Flask
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET KEY'] = 'b1b0c5e1b0712277e7037653e698fbe1f307ba5df7459a1ad7dbf4f801618e0d'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return('Hi!')

"""
Генерация надежного секртного кода
>>> import secrets
>>> secrets.token_hex()

"""


if __name__ == '__main__':
    app.run(debug=True)