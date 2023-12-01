# CRUD db
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"

db = SQLAlchemy(app)

TASKS = []


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


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
        task_name = request.form.get('task')

        if task_name:
            task = Task(name=task_name)
            db.session.add(task)
            db.session.commit()

        return redirect(url_for("task_list_view"))


# R (lista) z CRUD
@app.route("/tasks")
def task_list_view():
    return render_template(
        'task_list.html',
        tasks=Task.query.all()
    )


# R (szczegól) z CRUD
@app.route("/tasks/<int:task_id>")
def task_detail_view(task_id):
    task = Task.query.get_or_404(task_id)

    return render_template(
        'task_detail.html',
        task=task
    )


# U z CRUD
@app.route("/tasks/<int:task_id>/update", methods=["GET", "POST"])
def task_update_view(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == "GET":
        return render_template(
            'task_update.html',
            task=task
        )

    if request.method == "POST":
        updated_task = request.form.get('task')
        task.name = updated_task
        db.session.commit()

        return redirect(url_for("task_list_view"))


# D z CRUD
@app.route("/tasks/<int:task_id>/delete", methods=["GET", "POST"])
def task_delete_view(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == "GET":
        return render_template(
            'task_delete.html',
            task=task
        )

    if request.method == "POST":
        if "yes" in request.form:
            db.session.delete(task)
            db.session.commit()

        return redirect(url_for("task_list_view"))


if __name__ == "__main__":
    app.run(debug=True)
