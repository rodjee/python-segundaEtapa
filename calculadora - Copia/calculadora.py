import math
from flask import render_template, request

def calcular():
    try:
        num1_valor = request.form.get("num1", "").strip()
        if not num1_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o primeiro número.",
                resultados="",
            )

        num1 = float(num1_valor)
        operacao = request.form["operacao"]



        if operacao == "sqrt":
            if num1 < 0:
                etapas = f"Não existe raiz real de {num1}."
                resultados = "Erro: número negativo"
            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1}"
                resultados = resultado
            return render_template("calculadora.html", etapas=etapas, resultados=resultados)


        if operacao == "log":
            if num1 <= 0:
                etapas = f"Logaritmo indefinido para {num1}."
                resultados = "Erro: número deve ser maior que zero"
            else:
                resultado = math.log(num1)         
                etapas = f"ln({num1})"
                resultados = resultado
            return render_template("calculadora.html", etapas=etapas, resultados=resultados)

        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )

        num2 = float(num2_valor)
        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} − {num2}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} × {num2}"
        elif operacao == "/":
            if num2 == 0:
                return render_template(
                    "calculadora.html",
                    etapas=f"{num1} ÷ 0",
                    resultados="erro: divisão por zero",
                )
            resultado = num1 / num2
            etapas = f"{num1} ÷ {num2}"
        elif operacao == "**":
            resultado = math.pow(num1, num2)
            etapas = f"{num1} ^ {num2}"
        elif operacao == "log2":
            if num1 <= 0:
                return render_template(
                    "calculadora.html",
                    etapas=f"log base {num2} de {num1}",
                    resultados="numero tem q ser maior que zero",
                )

            if num2 <= 0 or num2 == 1:
                return render_template(
                    "calculadora.html",
                    etapas=f"log base {num2} de {num1}",
                    resultados="Erro: base invalida ",
                )
            resultado = math.log(num1, num2)
            etapas = f"log_{num2}({num1})"
        else:
            return render_template(
                "calculadora.html",
                etapas="Operação invalida."
            )

        if isinstance(resultado, float) and resultado.is_integer():
            resultados = int(resultado)
        else:
            resultados = round(resultado, 10)
        return render_template("calculadora.html", etapas=etapas, resultados=resultados)

    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Valor inválido. Use apenas números."
        )