from flask import Flask, render_template

app = Flask(__name__)

html = """
<h1>Привет, меня зовут Анна</h1>
<p>Уже много лет я создаю сайты на Flask.<br/>Посмотрите на мой сайт.</p>"""

@app.route('/')
def index():
    return 'Hi'

@app.route('/poems/')
def poems():
    context = {'poem': ['Вот не думал, не гадал,',
                        'Программистом взял и стал.',
                        'Хитрый знает он язык,',
                        'Он к другому не привык.',
                ]}
    # txt = """<h1>Стихотворение</h1>\n<p>""" + '<br/>'.join(poem) + '</p>'
    return render_template('poems.html', **context)


if __name__ =='__main__':
    app.run(debug=True)