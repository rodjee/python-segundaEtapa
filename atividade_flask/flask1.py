from flask import Flask

app = Flask(__name__)
@app.route('/decorator')
def decorator():
    return 'São funções especiais que modificam ou estendem o comportamento de outras funções ou métodos sem alterar seu código-fonte original. \nservem para modificar ou estender o comportamento de funções, métodos ou classes sem alterar seu código original. \nNo framework Flask, eles são essenciais e aparecem com a sintaxe @nome_do_decorator acima da definição da função'


if __name__ == '__main__':
    app.run(debug=True)