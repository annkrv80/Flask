from flask import Flask, render_template
import random
import os
from Task_01.models import db, Student, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.db'
db.init_app(app)

@app.route('/')
def index():
    return 'Hi!'

@app.cli.command("init-db")
def init_db():
    db.create_all()

@app.cli.command("fill-db")
def fill_db():
    for i in range(5):
        faculty = Faculty(name=f'faculty_{i}')
        db.session.add(faculty)
    for i in range(20):
        studetn = Student(
            name=f'name_{i}',
            surname=f'name_{i}',
            age=random.randint(18,25),
            gender=random.choice(["m", "f"]),
            group=f'group_{i}',
            faculty_id=random.randint(0,4)
        )
        db.session.add(studetn)
    db.session.commit()

@app.route('/get/')
def get():
    students = Student.query.all()
    return render_template('students.html', students=students)
    