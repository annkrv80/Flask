from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms_1 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b1b0c5e1b0712277e7037653e698fbe1f307ba5df7459a1ad7dbf4f801618e0d'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    return('Hi!')

@app.route('/data/')
def data():
    return 'Your data'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)