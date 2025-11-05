💻 Task 2 – React Frontend (Bonus Task)
📖 Project Overview

This is the frontend part of the Flask + React CRUD application.
It connects to the Flask backend APIs and allows users to add, edit, and delete tasks easily through a simple UI built with React + TypeScript + Vite.

⚙️ Tech Stack

React (vite + TypeScript)

Axios (for API calls)

Flask backend integration

HTML / CSS / JS

🚀 How to Run (Windows)

1️⃣ Navigate to the frontend folder

cd "D:\Rahul\.vscode\Better Solution\flask-react-crud\frontend"


2️⃣ Install dependencies

npm install


3️⃣ Start the frontend development server

npm run dev


Then open the app in your browser 👉 http://localhost:5173

🔗 Backend Connection

Make sure the Flask backend is running at
http://127.0.0.1:5000

before you start the React app.

If you use a different port, update API_BASE in:
📂 frontend/src/api.ts

export const API_BASE = "http://127.0.0.1:5000";

🧠 Main Features

✅ Add a new task
✅ Edit existing tasks
✅ Delete tasks
✅ Fetch and display tasks from the Flask backend

🖼️ Screenshots

Add your screenshots in a screenshots folder inside frontend/,
and reference them like this:

### 🏠 Home Page  
![Home Page](./screenshots/home.png)

### ➕ Add Task  
![Add Task](./screenshots/add-task.png)

### 🗑️ Delete Task  
![Delete Task](./screenshots/delete-task.png)

👨‍💻 Author

Rahul Kumar Bhakat
