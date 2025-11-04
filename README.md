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

## ⚙️ How to Run (Windows)

### 1. Setup Virtual Environment
```powershell
cd backend
python -m venv venv
.\venv\Scripts\activate
2. Install Required Packages
powershell
Copy code
pip install flask flask_sqlalchemy flask_marshmallow marshmallow marshmallow-sqlalchemy flask-cors pytest
3. Run the Server
powershell
Copy code
$env:FLASK_APP="app:create_app"
flask run
Now visit → http://127.0.0.1:5000

🔍 Check API Status
Health Check: http://127.0.0.1:5000/health

Ping: http://127.0.0.1:5000/api/ping








