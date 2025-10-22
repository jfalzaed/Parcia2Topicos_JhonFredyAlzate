from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/factorial/<int:n>", methods=["GET"])
def calcular_factorial(n):
    # Calculamos el factorial
    fact = math.factorial(n)
    # El factorial es par o impar
    paridad = "par" if fact % 2 == 0 else "impar"

    # La respuesta en JSON
    return jsonify({
        "numero recibido": n,
        "factorial": fact,
        "paridad": paridad
    })

if __name__ == "__main__":
    app.run(debug=True)
