from marshmallow import Schema, fields, validate

class CommentCreateSchema(Schema):
    body = fields.String(required=True, validate=validate.Length(min=1))
    author = fields.String(load_default="Anonymous", validate=validate.Length(max=120))

class CommentUpdateSchema(Schema):
    body = fields.String(validate=validate.Length(min=1))
    author = fields.String(validate=validate.Length(max=120))

class CommentOutSchema(Schema):
    id = fields.Int()
    task_id = fields.Int()
    body = fields.String()
    author = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
