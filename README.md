🧩 Task 1 – Flask Backend (Comments CRUD API)
📖 Project Overview

This is the backend part of a Flask + React CRUD application.
It provides REST APIs to add, view, update, and delete comments for a specific task.
The project follows clean code structure using Flask, SQLAlchemy, and Marshmallow.

⚙️ Tech Stack

Flask – Web framework

SQLite – Database

SQLAlchemy – ORM for database models

Marshmallow – For data validation and serialization

pytest – For testing

🚀 How to Run (Windows)

Open Terminal and Go to Backend Folder

cd "D:\Rahul\.vscode\Better Solution\flask-react-crud\backend"


Create and Activate Virtual Environment

python -m venv venv
.\venv\Scripts\activate


Install Required Packages

pip install flask flask_sqlalchemy flask_marshmallow marshmallow marshmallow-sqlalchemy flask-cors pytest


Run the Flask Server

$env:FLASK_APP="app:create_app"
flask run


Server will start at 👉 http://127.0.0.1:5000

🔍 API Endpoints
Method	Endpoint	Description
GET	/health	Check server health
GET	/api/ping	Test API connection
POST	/api/tasks/<task_id>/comments	Create a new comment
GET	/api/tasks/<task_id>/comments	List all comments for a task
GET	/api/comments/<comment_id>	Get a specific comment
PATCH	/api/comments/<comment_id>	Update a comment
DELETE	/api/comments/<comment_id>	Delete a comment
🧠 Example Request

POST /api/tasks/1/comments

{
  "body": "First comment!",
  "author": "Rahul"
}

✅ Testing

Run all backend tests:

pytest -q

👨‍💻 Author

Rahul Kumar Bhakat
