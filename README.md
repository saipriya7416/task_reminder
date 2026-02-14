# Task Reminder Web Application

## Overview
A simple web-based Task Reminder app built with Flask and SQLite. Users can add tasks, set deadlines, view all tasks, mark tasks as completed, and see overdue tasks highlighted in red.

## Features
- Add Task (Title + Deadline Date)
- Display Task List
- Mark Task as Completed
- Edit Task
- Overdue Tasks highlighted in red
- Basic input validation
- Clean folder structure

## Folder Structure
```
app.py              # Main Flask app
README.md           # Project documentation
static/
  style.css         # CSS styles
templates/
  index.html        # HTML UI
  edit.html         # Edit task form
```

## How to Run
1. Install dependencies:
   ```
   pip install flask flask_sqlalchemy
   ```
2. Create the database:
   ```
   python
   from app import app, db
   with app.app_context():
       db.create_all()
   exit()
   ```
3. Start the app:
   ```
   python app.py
   ```
4. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Key Learnings
- Flask routing and templates
- Using SQLAlchemy with SQLite
- Input validation and flash messages
- Git workflow and commit discipline
- UI feedback for overdue/completed tasks
- Debugging and error handling

## Git Commands
```powershell
git add .
git commit -m "Add feature: edit task"
git push
```

## Video Script
1. Brief intro: Project goal and features
2. Show app running: add, edit, mark done, overdue highlight
3. Explain code structure: app.py, templates, static
4. Share learnings and challenges
5. Show GitHub repo and README

## Submission
- GitHub repo link-https://github.com/saipriya7416/task_reminder.git
- Video file or link

## GitHub Repository
[https://github.com/saipriya7416/task_reminder](https://github.com/saipriya7416/task_reminder)
