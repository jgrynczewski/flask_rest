# CRUD
from flask import Flask, render_template, request, redirect, url_for, abort


app = Flask(__name__)

TASKS = []


# C z CRUD
@app.route('/tasks/create', methods=['GET', 'POST'])
def task_create_view():
    # GET
    if request.method == "GET":
        return render_template(
            'task_form.html',
        )

    # POST
    if request.method == "POST":
        task = request.form.get('task')
        if task:
            TASKS.append(task)

        return redirect(url_for("task_list_view"))


# R (lista) z CRUD
@app.route("/tasks")
def task_list_view():
    return render_template(
        'task_list.html',
        tasks=TASKS
    )


# R (szczegól) z CRUD
@app.route("/tasks/<int:task_id>")
def task_detail_view(task_id):
    if task_id <= 0 or task_id > len(TASKS):
        abort(404)

    task = TASKS[task_id-1]

    return render_template(
        'task_detail.html',
        task_id=task_id,
        task=task
    )

# U i D


if __name__ == "__main__":
    app.run(debug=True)
