from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity

from .models import Task

task = Blueprint('task', __name__, url_prefix="/api/v1/tasks")


@task.get("/tasks")
@jwt_required()
def task_list_view():
    user_id = get_jwt_identity()
    result = [{"id": task.id, "task": task.name} for task in Task.query.all()]
    return result
