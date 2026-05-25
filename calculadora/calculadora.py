import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

    

def calcular():
    numa = float(request.form['numa'])
    numb = float(request.form['numb'])
    operacao = resquest.form['operacao']

    if (operacao == '+'):
        resultado = numa + numb
        etapas = f'{numa} + {numb} = {resultado}'
       
    elif (operacao == '-'):
        resultado = numa - numb
        etapas = f'{numa} - {numb} = {resultado}'
        
    elif (operacao == '*'):
        resultado = numa * numb
        etapas = f'{numa} * {numb} = {resultado}'
        
    elif (operacao == '/'):
        if numb != 0 :
            resultado = numa / numb
            etapas = f'{numa} / {numb} = {resultado}'

        else :
            resultado = 'não da pra dividir por 0'
            etapas = 'não da pra dividir por 0'
        
       
       
    else :
        resultado = 'opção invalida'
        etapas = 'a operação selecionada é invalida'
    

    return render_template('index.html', etapas=etapas, resultados=resultado)

if __name__ == '__main__':
    app.run(debug=True)