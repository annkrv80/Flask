from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url
    }
    return render_template('404.html', **context)


if __name__ == '__main__':
    app.run(debug=True)