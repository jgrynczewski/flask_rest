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


# U z CRUD
@app.route("/tasks/<int:task_id>/update", methods=["GET", "POST"])
def task_update_view(task_id):
    if task_id <= 0 or task_id > len(TASKS):
        abort(404)

    task = TASKS[task_id - 1]

    if request.method == "GET":

        return render_template(
            'task_update.html',
            task_id=task_id,
            task=task
        )

    if request.method == "POST":
        updated_task = request.form.get('task')
        TASKS[task_id - 1] = updated_task

        return redirect(url_for("task_list_view"))


# D z CRUD
@app.route("/tasks/<int:task_id>/delete", methods=["GET", "POST"])
def task_delete_view(task_id):
    if task_id <= 0 or task_id > len(TASKS):
        abort(404)

    task = TASKS[task_id -1 ]

    if request.method == "GET":
        return render_template(
            'task_delete.html',
            task_id=task_id,
            task=task
        )

    if request.method == "POST":
        if "yes" in request.form:
            TASKS.pop(task_id-1)

        return redirect(url_for("task_list_view"))


if __name__ == "__main__":
    app.run(debug=True)
