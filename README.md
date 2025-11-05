# Software Engineer – Assessment (Better Software)

## Status (My Submission)
- ✅ **Task #1 (Comments CRUD + Tests): Completed**
- ✅ **Task #2 (Tasks UI – Bonus): Completed**
- 📦 **Default branch `main` contains the final working solution for both tasks.**
- 🌿 Separate branches maintained for isolated history/review:
  - **Task 1 branch:** `<your-task1-branch>` (e.g., `feat/task1-comments-crud`)
  - **Task 2 branch:** `<your-task2-branch>` (e.g., `feat/task2-tasks-ui`)

> Reviewers can evaluate via PRs from the branches into `main` (links below).

---

## Role Overview
We build high-quality, scalable software from the ground up. As a **Software Engineer**, I implemented robust, maintainable solutions using **TypeScript, React, and Python**, focusing on clean code, tests, and clear API design.

## About Better Software
Better Software is an AI-powered agency for web, mobile, and custom apps with strong engineering foundations. Over 7 years, they’ve worked with bootstrapped companies generating **$100M+**, unicorns, **Techstars** startups, and leaders from **Apple** and **Google**, including top VCs like **Andreessen Horowitz**.

---

## Assessment Summary

### Task #1 (Required): Comments CRUD APIs + Tests
- Built RESTful endpoints to **create, read, update, delete** comments for a given task.
- Followed proper HTTP semantics, validation, and error handling.
- Added **automated tests** (unit/integration) covering happy paths and edge cases.

### Task #2 (Bonus): Tasks UI (React)
- Built a minimal frontend to **add, edit, delete** tasks using existing CRUD APIs.
- Included UX touches for validation and feedback.
- Kept code modular and easy to extend.

---

## Branch & PR Links
> PRs are raised **against my fork’s `main`** so each task can be reviewed independently.

- **Task #1 PR:** `<link-to-PR-from-<your-task1-branch>-to-main>`
- **Task #2 PR:** `<link-to-PR-from-<your-task2-branch>-to-main>`

Branches:
- Task 1: `<your-task1-branch>`
- Task 2: `<your-task2-branch>`
- Final merged: `main`

---

## How to Run

### Backend (Flask)
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
# If using migrations:
flask db upgrade
flask run

