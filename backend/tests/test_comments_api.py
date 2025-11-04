import pytest
from app import create_app, db
from app.models import Task

@pytest.fixture
def app():
    class TestConfig:
        TESTING = True
        SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    app = create_app(TestConfig)
    with app.app_context():
        db.drop_all()
        db.create_all()
        db.session.add(Task(title="Sample Task"))
        db.session.commit()
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_comment(client):
    r = client.post("/api/tasks/1/comments", json={"body": "Hi", "author": "Rahul"})
    assert r.status_code == 201
    data = r.get_json()
    assert data["body"] == "Hi"

def test_create_comment_requires_body(client):
    r = client.post("/api/tasks/1/comments", json={})
    assert r.status_code == 400

def test_list_comments(client):
    client.post("/api/tasks/1/comments", json={"body": "A"})
    client.post("/api/tasks/1/comments", json={"body": "B"})
    r = client.get("/api/tasks/1/comments")
    assert r.status_code == 200
    assert r.get_json()["count"] == 2

def test_get_update_delete_comment(client):
    c = client.post("/api/tasks/1/comments", json={"body": "X"}).get_json()
    cid = c["id"]

    assert client.get(f"/api/comments/{cid}").status_code == 200
    assert client.patch(f"/api/comments/{cid}", json={"body": "Y"}).status_code == 200
    assert client.delete(f"/api/comments/{cid}").status_code == 204
