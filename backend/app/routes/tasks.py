# backend/app/routes/tasks.py
from flask import Blueprint, request, jsonify
from .. import db
from ..models import Task
from ..schemas import TaskCreateSchema, TaskUpdateSchema, TaskOutSchema

bp = Blueprint("tasks", __name__, url_prefix="/api")

create_in = TaskCreateSchema()
update_in = TaskUpdateSchema()
task_out = TaskOutSchema()
tasks_out = TaskOutSchema(many=True)

@bp.route("/tasks", methods=["GET"])
def list_tasks():
    limit = min(int(request.args.get("limit", 50)), 100)
    offset = int(request.args.get("offset", 0))
    q = Task.query.order_by(Task.created_at.desc())
    items = q.offset(offset).limit(limit).all()
    return jsonify({"items": tasks_out.dump(items), "count": q.count(), "limit": limit, "offset": offset})

@bp.route("/tasks", methods=["POST"])
def create_task():
    data = create_in.load(request.get_json() or {})
    t = Task(title=data["title"], description=data.get("description"))
    db.session.add(t)
    db.session.commit()
    return jsonify(task_out.dump(t)), 201

@bp.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id: int):
    t = Task.query.get_or_404(task_id, description="Task not found")
    return jsonify(task_out.dump(t))

@bp.route("/tasks/<int:task_id>", methods=["PATCH"])
def update_task(task_id: int):
    t = Task.query.get_or_404(task_id, description="Task not found")
    data = update_in.load(request.get_json() or {}, partial=True)
    for k, v in data.items():
        setattr(t, k, v)
    db.session.commit()
    return jsonify(task_out.dump(t))

@bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id: int):
    t = Task.query.get_or_404(task_id, description="Task not found")
    db.session.delete(t)
    db.session.commit()
    return "", 204
