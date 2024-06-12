from flask import Flask, jsonify, request
import math
import statistics

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify(error="Missing parameters"), 400
    return jsonify(result=a + b)

@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify(error="Missing parameters"), 400
    return jsonify(result=a - b)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify(error="Missing parameters"), 400
    return jsonify(result=a * b)

@app.route('/divide', methods=['GET'])
def divide():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify(error="Missing parameters"), 400
    if b == 0:
        return jsonify(error="Division by zero"), 400
    return jsonify(result=a / b)

@app.route('/factorial', methods=['GET'])
def factorial():
    n = request.args.get('n', type=int)
    if n is None:
        return jsonify(error="Missing parameter"), 400
    if n < 0:
        return jsonify(error="Factorial is not defined for negative numbers"), 400
    return jsonify(result=math.factorial(n))

@app.route('/sqrt', methods=['GET'])
def sqrt():
    x = request.args.get('x', type=float)
    if x is None:
        return jsonify(error="Missing parameter"), 400
    if x < 0:
        return jsonify(error="Square root is not defined for negative numbers"), 400
    return jsonify(result=math.sqrt(x))

@app.route('/power', methods=['GET'])
def power():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is None or b is None:
        return jsonify(error="Missing parameters"), 400
    return jsonify(result=math.pow(a, b))

@app.route('/median', methods=['GET'])
def median():
    values = request.args.getlist('values', type=float)
    if not values:
        return jsonify(error="Missing parameters"), 400
    return jsonify(result=statistics.median(values))

if __name__ == '__main__':
    app.run(debug=True)
