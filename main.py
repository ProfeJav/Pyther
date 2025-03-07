from flask import Flask, render_template, request
import os
import requests
import random

app = Flask(__name__)

# API gratuita de números
API_URL = "http://numbersapi.com/"

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    numero = random.randint(1, 100)  # Número aleatorio inicial

    if request.method == "POST":
        try:
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])

            # Operaciones matemáticas
            suma = num1 + num2
            resta = num1 - num2
            multiplicacion = num1 * num2
            division = num1 / num2 if num2 != 0 else "No se puede dividir por 0"

            resultado = {
                "suma": suma,
                "resta": resta,
                "multiplicacion": multiplicacion,
                "division": division
            }

            # Consultar información sobre el número ingresado
            numero = num1
        except ValueError:
            resultado = {"error": "Ingresa valores numéricos válidos"}

    # Consultar API de NumbersAPI
    response = requests.get(f"{API_URL}{numero}")
    info_numero = response.text if response.status_code == 200 else "No se encontró información"

    return render_template("index.html", numero=numero, info_numero=info_numero, resultado=resultado)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Obtiene el puerto de Azure o usa 8000 por defecto
    app.run(host="0.0.0.0", port=port, debug=True)
