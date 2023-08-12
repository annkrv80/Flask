from flask import Flask, request, redirect, flash, render_template, url_for

app = Flask(__name__)

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
    # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('form'))
# Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')


if __name__ =="__main__":
    app.run(debug=True)