from flask import Flask, flash, redirect, render_template,request, url_for
app = Flask(__name__)
app.secret_key =b'10a0438f6ccdafce399c157715233bca94a0722378fe31f4c7713b5d6c09696e'
"""
Генерация секретного ключа
>>>import secrets
>>>secrets.token_hex()
"""
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
    # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('flash_form.html')

if __name__ == '__main__':
    app.run(debug=True)