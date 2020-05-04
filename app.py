from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("app.html")


@app.route("/calculate", methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']

    if operation == 'add':
        result = float(num1) + float(num2)
        return render_template('app.html', result=result)

    elif operation == 'subtract':
        result = float(num1) - float(num2)
        return render_template('app.html', result=result)

    elif operation == 'multiply':
        result = float(num1) * float(num2)
        return render_template('app.html', result=result)

    elif operation == 'divide':
        result = float(num1) / float(num2)
        return render_template('app.html', result=result)
    else:
        return render_template('app.html')
