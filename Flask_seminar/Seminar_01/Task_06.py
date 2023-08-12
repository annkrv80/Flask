#Написать функцию, которая будет выводить на экран HTML
#страницу с таблицей, содержащей информацию о студентах.
#Таблица должна содержать следующие поля:
# "Имя","Фамилия", "Возраст", "Средний балл".
#Данные о студентах должны быть переданы в шаблон через
#контекст.

from flask import Flask, render_template

app = Flask(__name__)

students = [
    {'firstname': 'Иван', 'lastname':'Иванов', 'age' : 23, 'rate' : 4.3},
    {'firstname': 'Сергей', 'lastname':'Сергеев', 'age' : 25, 'rate' : 3.5},
    {'firstname': 'Максим', 'lastname':'Максимов', 'age' : 20, 'rate' : 4.1}
]

@app.route('/')
def index():
    return 'Hi!'

@app.route('/student/')
def get_students():
    return render_template('students.html', students = students)


if __name__ == '__main__':
    app.run(debug=True)