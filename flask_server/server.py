import random
import datetime as dt
from flask import Flask, request, render_template


app = Flask(
    __name__,
    template_folder='templates'
)


@app.route('/')
def home_page():
    return "Welcome to Flask World!"


@app.route('/hello/<name>')
def hello_user(name):
    return f"Hello, {name}!"


@app.route('/hello')
def hello():
    name = request.args.get('name')
    year = request.args.get('year')
    month = request.args.get('month')
    return f"Hello, {name} {year} {month}!"


@app.route('/calculate/<int:a>/<int:b>')  # Route -> Registered URL in Flask
def calculate(a, b):  # View -> Will Run Function when Route if found by Flask
    operator = request.args.get('operator')  # Query Param is not strictly required in View function
    if operator == 'plus':
        result = a + b
    elif operator == 'minus':
        result = a - b
    elif operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    else:
        result = None

    return f"Result is: {result}"


@app.route('/template')
def template():
    current = dt.datetime.now()
    users = ['Andrew', 'Kate', 'Joe', 'Dan', 'Harry']
    random_number = random.randint(1, 10)
    return render_template('index.html', current_datetime=current, users=users, random_number=random_number)


app.run(
    host='localhost',
    port=5000,
    debug=True
)