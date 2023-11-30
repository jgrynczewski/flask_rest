from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

TASKS = []


@app.route('/tasks/create1')
def register_task():
    task = request.args.get('task')
    if task:
        TASKS.append(task)

    return render_template('form.html', tasks=TASKS)


@app.route('/tasks/create2', methods=['GET', 'POST'])
def register_task2():
    task = request.form.get('task')
    if task:
        TASKS.append(task)

    return render_template('form2.html', tasks=TASKS)


@app.route('/tasks/create3', methods=['GET', 'POST'])
def register_task3():
    # GET
    if request.method == "GET":
        return render_template(
            'form2.html',
            tasks=TASKS
        )

    # POST
    if request.method == "POST":
        task = request.form.get('task')
        if task:
            TASKS.append(task)

        return redirect(url_for("register_task3"))


if __name__ == "__main__":
    app.run(debug=True)
