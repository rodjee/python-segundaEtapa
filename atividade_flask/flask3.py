from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sobre/<nome>')
def sobre(nome):
    return f'Olá, {nome}! Bem vindo.'


if __name__ == '__main__':
    app.run(debug=True)