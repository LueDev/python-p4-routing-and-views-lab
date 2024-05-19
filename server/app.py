#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<parameter>")
def parameterized_route(parameter):
    print(parameter)
    return f"{parameter}"

@app.route("/count/<parameter>")
def count(parameter):
    str_count = ""
    for num in range(int(parameter)):
        str_count += f"{num}\n"
        print(num)
    return str_count

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    num1, num2 = int(num1), int(num2)
    mathy = {'+': num1 + num2, 
             '-': num1 - num2,
             '*': num1 * num2,
             'div': num1 / num2,
             '%': num1 % num2}
    print(mathy.get(operation, None))
    return str(mathy.get(operation, None))

if __name__ == '__main__':
    app.run(port=5555, debug=True)

