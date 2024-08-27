#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:number>')
def count(number):
    count_string = '\n'.join([str(i) for i in range(number)]) + '\n'
    return count_string

@app.route('/math/<int:parameter1>/<operation>/<int:parameter2>')
def math_operation(parameter1, operation, parameter2):
    if operation == '+':
        result = parameter1 + parameter2
    elif operation == '-':
        result = parameter1 - parameter2
    elif operation == '*':
        result = parameter1 * parameter2
    elif operation == 'div':
        result = parameter1 / parameter2
    elif operation == '%':
        result = parameter1 % parameter2
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
