# backend/app/schemas.py
from marshmallow import Schema, fields, validate

# ---------- Comment Schemas ----------
class CommentCreateSchema(Schema):
    body = fields.String(required=True, validate=validate.Length(min=1))
    author = fields.String(load_default="Anonymous")

class CommentUpdateSchema(Schema):
    body = fields.String(validate=validate.Length(min=1))
    author = fields.String()

class CommentOutSchema(Schema):
    id = fields.Int()
    task_id = fields.Int()
    body = fields.String()
    author = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

# ---------- Task Schemas ----------
class TaskCreateSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String(load_default=None)

class TaskUpdateSchema(Schema):
    title = fields.String(validate=validate.Length(min=1))
    description = fields.String(load_default=None)
    status = fields.String(validate=validate.OneOf(["todo", "in_progress", "done"]))

class TaskOutSchema(Schema):
    id = fields.Int()
    title = fields.String()
    description = fields.String(allow_none=True)
    status = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

