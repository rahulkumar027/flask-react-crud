# Flask + React CRUD (Assessment – Task #1)

This project implements **Task #1** of the assessment for the role of **Associate Software Engineer (Python / React)**.

It contains a **Flask-based backend** that provides clean, well-structured APIs to **add, edit, delete, and list comments** for a given **Task**, following proper CRUD principles.

---

## 👨‍💻 Author
**Name:** Rahul Kumar Bhakat  
**Email:** rahulkumarbhakat27@gmail.com  
**GitHub:** [rahulkumar027](https://github.com/rahulkumar027)

---

## 🧠 About the Project

This backend project was built using **Flask**, **SQLAlchemy**, and **Marshmallow** to demonstrate a strong foundation in API design, database modeling, and clean code architecture.

- Task #1: **Backend APIs for Comments CRUD + Automated Tests**
- Task #2 (Bonus): **React Frontend (to be added later)**

---

## 🧩 Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy, Marshmallow, Flask-CORS  
- **Database:** SQLite (dev.db)  
- **Testing:** Pytest  
- **Frontend:** React (for Task #2 - planned)

---
## Project Structure (relevant to Task #1)

backend/
app/
init.py # app factory, CORS, blueprint, health
models.py # Task, Comment models
schemas.py # Marshmallow schemas
routes/
comments.py # /api routes for comments (+ /api/ping)
tests/
test_comments_api.py
dev.db # created on first run (SQLite)



---

## Prerequisites
- Python 3.10+  
- Git (optional)  
- PowerShell (Windows) or bash (macOS/Linux)

---

## Run Locally

### 1) Create & activate a virtual environment
**Windows (PowerShell)**
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
macOS/Linux


cd backend
python3 -m venv venv
source venv/bin/activate
2) Install dependencies

pip install flask flask_sqlalchemy flask_marshmallow marshmallow marshmallow-sqlalchemy flask-cors pytest
3) Start the server
Windows

$env:FLASK_APP="app:create_app"
flask run
macOS/Linux

export FLASK_APP=app:create_app
flask run
Server runs at: http://127.0.0.1:5000

4) Quick health check
Open:

GET /health → http://127.0.0.1:5000/health → {"status":"ok"}

GET /api/ping → http://127.0.0.1:5000/api/ping → {"ok": true}

5) Seed one Task (so comments can attach)
Windows

python -c "from app import create_app, db; from app.models import Task; a=create_app(); c=a.app_context(); c.push(); t=Task(title='Seed Task'); db.session.add(t); db.session.commit(); print('TASK_ID=', t.id); c.pop()"
macOS/Linux

python - << 'PY'
from app import create_app, db
from app.models import Task
a = create_app()
with a.app_context():
    t = Task(title="Seed Task")
    db.session.add(t); db.session.commit()
    print("TASK_ID=", t.id)
PY
Note the printed TASK_ID (e.g., 1) and use it below.

API (Task #1)
Base URL: http://127.0.0.1:5000

Create comment
POST /api/tasks/<task_id>/comments
Body:

{ "body": "First comment!", "author": "Rahul" }
List comments
GET /api/tasks/<task_id>/comments
Query (optional): limit, offset
Response:

{ "items": [...], "count": 1, "limit": 50, "offset": 0 }
Get one comment
GET /api/comments/<id>

Update comment
PATCH /api/comments/<id>
Body (any):

{ "body": "Edited text" }
Delete comment
DELETE /api/comments/<id> → 204 No Content

Errors
400 → validation error (JSON object with details)

404 → not found (e.g., missing task/comment)

Run Tests
From backend/ (venv active):

pytest -q
Notes
SQLite path is absolute in the app, so CLI and server share the same dev.db.

Use Postman/PowerShell/curl for POST/PATCH/DELETE (browser address bar does GET only).

CORS enabled for /api/*.


Want me to also add a short **Task #2 (React) starter** section to the README so you can extend it later?







