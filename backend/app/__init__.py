# backend/app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

db = SQLAlchemy()
ma = Marshmallow()

# Absolute SQLite path so CLI and server use the same DB
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "dev.db")

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{DB_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False

def create_app(config_object: type | None = None):
    app = Flask(__name__)
    app.config.from_object(Config if config_object is None else config_object)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    ma.init_app(app)

    # Import models before creating tables
    from . import models  # noqa: F401

    # ✅ Register blueprints
    from .routes.comments import bp as comments_bp
    app.register_blueprint(comments_bp)

    from .routes.tasks import bp as tasks_bp
    app.register_blueprint(tasks_bp)

    # Root and health endpoints
    @app.route("/")
    def home():
        return {
            "message": "Flask API is running",
            "endpoints": [
                "/health",
                "/api/ping",
                "/api/tasks",
                "/api/tasks/<task_id>/comments"
            ],
        }

    @app.route("/health")
    def health():
        return {"status": "ok"}

    with app.app_context():
        db.create_all()

    return app
