import datetime

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/home")
def hello():
    return "Hello, world!"


@app.route("/hello/eva")
def hello_eva():
    return "Hello, Eva!"


@app.route("/hello/adam")
def hello_adam():
    return "Hello, Adam!"


@app.route("/hello/<name>")
def hello_name(name):
    name = escape(name)
    return f"Hello, {name}!"


@app.route("/hello2")
def hello2():
    return """
    <!DOCTYPE html>
    <html lang='en'>
        <head>
        </head>
        <body>
            <p>Hello, world!</p>
        </body>
    </html>
    """


@app.route("/hello3")
def hello_view():
    return render_template('hello.html')


@app.route("/hello3/<name>")
def hello_view3(name):
    return render_template(
        'hello.html',
        name=name
    )


@app.route("/isitnewyear")
def new_year():
    now = datetime.datetime.now()
    if now.day == 1 and now.month == 1:
        is_new_year = True
    else:
        is_new_year = False

    return render_template('isitnewyear.html', is_new_year=is_new_year)

@app.route("/jinja")
def jinja():

    class Cow():
        def __init__(self, name, age):
            self.name = name
            self.age = age

    return render_template(
        "jinja.html",
        fruits=[
            "jablko",
            "banan",
            "gruszka"
        ],
        user={
            "name": "John",
            "surename": "Doe",
            "age": 20
        },
        cow=Cow("Mućka", 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
