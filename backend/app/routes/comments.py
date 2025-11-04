# backend/app/routes/comments.py
from flask import Blueprint, request, jsonify, abort
from marshmallow import ValidationError
from .. import db
from ..models import Task, Comment
from ..schemas import CommentCreateSchema, CommentUpdateSchema, CommentOutSchema

bp = Blueprint("comments", __name__, url_prefix="/api")

@bp.route("/ping", methods=["GET"])
def ping():
    return {"ok": True}

create_in = CommentCreateSchema()
update_in = CommentUpdateSchema()
comment_out = CommentOutSchema()
comments_out = CommentOutSchema(many=True)

# ---------- Error handlers (JSON instead of HTML) ----------
@bp.app_errorhandler(ValidationError)
def on_validation_error(err: ValidationError):
    return jsonify({"error": "validation_error", "details": err.messages}), 400

@bp.app_errorhandler(404)
def on_404(err):
    # err.description may contain our custom message (e.g., "Task not found")
    return jsonify({"error": "not_found", "message": getattr(err, "description", "Not Found")}), 404
# -----------------------------------------------------------

def get_task_or_404(task_id: int) -> Task:
    task = Task.query.get(task_id)
    if not task:
        abort(404, description="Task not found")
    return task

@bp.route("/tasks/<int:task_id>/comments", methods=["POST"])
def create_comment(task_id: int):
    get_task_or_404(task_id)
    payload = request.get_json() or {}
    data = create_in.load(payload)       # raises ValidationError -> handled above as 400
    c = Comment(task_id=task_id, **data)
    db.session.add(c)
    db.session.commit()
    return jsonify(comment_out.dump(c)), 201

@bp.route("/tasks/<int:task_id>/comments", methods=["GET"])
def list_comments(task_id: int):
    get_task_or_404(task_id)
    limit = min(int(request.args.get("limit", 50)), 100)
    offset = int(request.args.get("offset", 0))
    q = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.desc())
    items = q.offset(offset).limit(limit).all()
    return jsonify({
        "items": comments_out.dump(items),
        "count": q.count(),
        "limit": limit,
        "offset": offset
    })

@bp.route("/comments/<int:comment_id>", methods=["GET"])
def get_comment(comment_id: int):
    c = Comment.query.get_or_404(comment_id, description="Comment not found")
    return jsonify(comment_out.dump(c))

@bp.route("/comments/<int:comment_id>", methods=["PATCH"])
def update_comment(comment_id: int):
    c = Comment.query.get_or_404(comment_id, description="Comment not found")
    payload = request.get_json() or {}
    data = update_in.load(payload, partial=True)  # ValidationError -> 400
    for k, v in data.items():
        setattr(c, k, v)
    db.session.commit()
    return jsonify(comment_out.dump(c))

@bp.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id: int):
    c = Comment.query.get_or_404(comment_id, description="Comment not found")
    db.session.delete(c)
    db.session.commit()
    return "", 204

