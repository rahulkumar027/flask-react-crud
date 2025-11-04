# flask-react-crud
Flask + React CRUD App (Assessment Task)
# flask-react-crud

Flask + React CRUD App (Assessment Task)

This project implements **Task #1** of the assessment:
- **Backend (Flask + SQLAlchemy + Marshmallow)** with clean CRUD APIs for **Comments** under a **Task**.
- Includes **error handling**, **pagination-ready list**, and **automated tests** using **pytest**.
- (Bonus **Task #2 – React UI**: section reserved below; wire-up TBD.)

---

## ✨ Features

- **Flask Blueprint**-based API under `/api/*`
- **SQLite** local database (absolute path to avoid path mismatches)
- **Models**: `Task`, `Comment` (1-to-many)
- **Validation**: Marshmallow schemas for create/update
- **CORS**: enabled for `/api/*`
- **Automated tests**: pytest fixtures + in-memory DB
- **Dev ergonomics**: `/health` and `/api/ping` endpoints for quick checks

---

## 🧱 Tech Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy, Marshmallow, Flask-CORS
- **DB**: SQLite (file: `backend/dev.db`)
- **Tests**: Pytest
- **Frontend**: React (placeholder for Task #2)

---

## 📁 Project Structure

<img width="711" height="460" alt="image" src="https://github.com/user-attachments/assets/d4e31731-a467-43f9-ae0a-48b07748ca6a" />


## 🚀 Quick Start

> You can run with **Windows PowerShell** or **macOS/Linux bash**.  
> Python 3.10+ recommended.

### 1) Create & activate virtual env

**Windows (PowerShell)**
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
macOS/Linux

bash
Copy code
cd backend
python3 -m venv venv
source venv/bin/activate
2) Install dependencies
bash
Copy code
pip install flask flask_sqlalchemy flask_marshmallow marshmallow marshmallow-sqlalchemy flask-cors pytest
marshmallow-sqlalchemy silences a warning and plays nice with flask-marshmallow.

3) Run the server
Windows (PowerShell)

powershell
Copy code
$env:FLASK_APP="app:create_app"
flask run
macOS/Linux

bash
Copy code
export FLASK_APP=app:create_app
flask run
Server starts at: http://127.0.0.1:5000

4) Sanity checks
Open in a browser or use curl/PowerShell:

Health:

GET http://127.0.0.1:5000/health → {"status":"ok"}

Blueprint live:

GET http://127.0.0.1:5000/api/ping → {"ok": true}

🌱 Seeding a Task (so you can attach comments)
Windows (PowerShell)

powershell
Copy code
python -c "from app import create_app, db; from app.models import Task; a=create_app(); c=a.app_context(); c.push(); t=Task(title='Seed Task', description='for comments testing'); db.session.add(t); db.session.commit(); print('TASK_ID=', t.id); c.pop()"
macOS/Linux

bash
Copy code
python - << 'PY'
from app import create_app, db
from app.models import Task
a = create_app()
with a.app_context():
    t = Task(title="Seed Task", description="for comments testing")
    db.session.add(t)
    db.session.commit()
    print("TASK_ID=", t.id)
PY
Note the printed TASK_ID (e.g., 1). Use it in the endpoints below.

🔌 API Reference
Base URL: http://127.0.0.1:5000

Health / Ping
GET /health → {"status":"ok"}

GET /api/ping → {"ok": true}

Comments (under a Task)
Create Comment
POST /api/tasks/<task_id>/comments
Body:

json
Copy code
{
  "body": "First comment!",
  "author": "Rahul"
}
Returns 201 with created comment.

List Comments
GET /api/tasks/<task_id>/comments
Query (optional): limit (default 50, max 100), offset (default 0)
Returns:

json
Copy code
{
  "items": [...],
  "count": 2,
  "limit": 50,
  "offset": 0
}
Get One
GET /api/comments/<id>

Update
PATCH /api/comments/<id>
Body (any of):

json
Copy code
{ "body": "Edited text" }
Delete
DELETE /api/comments/<id> → 204 No Content

Error Handling
400 with { "error": "validation_error", "details": {...} }

404 with { "error": "not_found", "message": "Task not found" }

🧪 Running Tests
From backend/ with venv active:

bash
Copy code
pytest -q
The test suite uses an in-memory SQLite DB and seeds a Task fixture, then verifies:

create/list/get/patch/delete comment

pagination surface

404 when Task missing

400 validation errors

🖥️ Example Requests (PowerShell)
powershell
Copy code
# List (GET)
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/tasks/1/comments"

# Create (POST)
$body = @{ body = "First comment!"; author = "Rahul" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/tasks/1/comments" -Method POST -ContentType "application/json" -Body $body

# Update (PATCH)
$patch = @{ body = "Edited text" } | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/comments/1" -Method PATCH -ContentType "application/json" -Body $patch

# Delete (DELETE)
Invoke-WebRequest -Uri "http://127.0.0.1:5000/api/comments/1" -Method DELETE
⚠️ Common Pitfalls & Fixes
404 Not Found on POST in browser
The browser sends GET. Use PowerShell/curl/Postman for POST/PATCH/DELETE.

Task not found (404)
Seed a Task first (see Seeding section) and use that real <task_id>.

Using different DB files
This repo sets an absolute SQLite path in app/__init__.py so CLI and server share the same dev.db.

“Flask-SQLAlchemy integration requires marshmallow-sqlalchemy” warning
Install: pip install marshmallow-sqlalchemy (optional, cleans up logs).

Windows PowerShell vs bash
PowerShell doesn’t support bash heredocs or mkdir -p. Use the provided Windows commands.

🧭 Development Notes
App factory: app:create_app

CORS enabled for /api/*

Pagination ready in list endpoint

Easy to extend with auth, pagination params, or rate limiting

🧪 Task #1 Status
✅ Completed: Backend Comments CRUD + Tests.

PR branch example: task1-comments-crud

Suggested PR title: Task #1 – Comments CRUD APIs + Automated Tests
