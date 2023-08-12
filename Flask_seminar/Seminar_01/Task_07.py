#Написать функцию, которая будет выводить на экран HTML
#страницу с блоками новостей.
#Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
#Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

app = Flask(__name__)

class News:
    def __init__(self, title, description, data):
        self.title = title
        self.description = description
        self.data = data


@app.route('/')
def news():
    news = [News('Какая-то новость', 'Описание', '2023-08-04'),
            News('Какая-то новость', 'Описание', '2023-08-04'),
            News('Какая-то новость', 'Описание', '2023-08-04'),
            News('Какая-то новость', 'Описание', '2023-08-04'),
            News('Какая-то новость', 'Описание', '2023-08-04'),
            News('Какая-то новость', 'Описание', '2023-08-04'),
            ]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)