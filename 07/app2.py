# CRUD db
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy

from flask_swagger_ui import get_swaggerui_blueprint
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"

swagger_blueprint = get_swaggerui_blueprint('/swagger', '/static/swagger.json')
app.register_blueprint(swagger_blueprint)


db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)


class TaskSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name'
        )


task_schema = TaskSchema(many=False)
tasks_schema = TaskSchema(many=True)

# C z CRUD
@app.post('/tasks')
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
@app.get("/tasks")
def task_list_view():
    tasks = Task.query.all()
    result = tasks_schema.dump(tasks)

    return result


# R (szczegól) z CRUD
@app.get("/tasks/<int:task_id>")
def task_detail_view(task_id):
    task = Task.query.get(task_id)

    if not task:
        return {
            "msg": "Resource not found"
        }, 404

    result = task_schema.jsonify(task)
    return result


# U z CRUD
@app.put("/tasks/<int:task_id>")
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
@app.delete("/tasks/<int:task_id>")
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
