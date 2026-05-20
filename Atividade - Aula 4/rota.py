from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobremim')
def sobremim():
    return render_template('sobremim.html')

@app.route('/expectativas')
def expectativa():
    return render_template('expectativas.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')


@app.route('/layout')
def layout():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)