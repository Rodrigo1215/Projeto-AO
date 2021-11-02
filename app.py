from flask import render_template, Flask
app = Flask('')


'''
Escreva os Controllers neste arquivo
'''
@app.route('/')
def principal():
    return render_template('pagina1.html')


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')