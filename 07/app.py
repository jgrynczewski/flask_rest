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
@app.route('/tasks', methods=['POST'])
def task_create_view():
    task_name = request.json.get('name')

    if task_name:
        task = Task(name=task_name)
        db.session.add(task)
        db.session.commit()

        return {
            "msg": "New task created",
            "name": task.name
        }, 201

    return {
        "msg": "Wrong request"
    }, 400


# R (lista) z CRUD
@app.route("/tasks")
def task_list_view():
    result = [{"id": task.id, "task": task.name} for task in Task.query.all()]
    return result


# R (szczegól) z CRUD
@app.route("/tasks/<int:task_id>")
def task_detail_view(task_id):
    task = Task.query.get(task_id)

    if not task:
        return {
            "msg": "Resource not found"
        }, 404

    return {
        "id": task.id,
        "name": task.name
    }


# U z CRUD
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def task_update_view(task_id):
    task = Task.query.get(task_id)

    if not task:
        return {
            "msg": "Resource not found"
        }, 404

    task_name_updated = request.json.get('name')
    task.name = task_name_updated
    db.session.commit()

    return {
        "msg": "Resource updated"
    }


# D z CRUD
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def task_delete_view(task_id):
    task = Task.query.get(task_id)
    if not task:
        return {
            "msg": "Resource not found"
        }, 404

    db.session.delete(task)
    db.session.commit()

    return {
        "msg": "Resource deleted"
    }


if __name__ == "__main__":
    app.run(debug=True)

