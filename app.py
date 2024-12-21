from flask import Flask, jsonify, redirect, url_for
import math

app = Flask(__name__)

# Fonction pour effectuer l'intégration numérique
def numerical_integration(lower, upper, N):
    step = (upper - lower) / N
    total_area = 0.0
    for i in range(N):
        x = lower + i * step
        total_area += math.fabs(math.sin(x)) * step
    return total_area

# Route par défaut
@app.route('/')
def default_route():
    return redirect(url_for('integrate', lower=0, upper=3.14159))

# Endpoint pour l'intégration numérique
@app.route('/numericalintegralservice/<lower>/<upper>/', methods=['GET'])
@app.route('/numericalintegralservice/<lower>/<upper>', methods=['GET'])
def integrate(lower, upper):
    try:
        lower = float(lower)
        upper = float(upper)
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide valid float numbers."}), 400

    print(f"Received request for lower={lower}, upper={upper}")
    N_values = [10, 50, 100, 1000, 10000, 100000, 1000000]  # Différentes valeurs de N
    results = []

    for N in N_values:
        result = numerical_integration(lower, upper, N)
        results.append({"N": N, "Result": result})

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
