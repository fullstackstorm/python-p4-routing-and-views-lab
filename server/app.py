#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string>')
def print_string(string):
    response = f"{string}"
    print(response)
    return response

@app.route('/count/<int:num>')
def count(num):
    retval = ''
    for number in range(num):
        retval += f'{number}\n'
        print(f'{number}')
    return retval

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        'div': lambda x, y: x / y if y != 0 else "Error: Division by zero",
        '%': lambda x, y: x % y,
    }

    result = operations.get(operation, lambda x, y: "Invalid operation")(num1, num2)
    return f"{result}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
