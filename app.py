from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change to any random string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    deadline = db.Column(db.String(10), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.title}>'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        deadline = request.form.get('deadline', '').strip()
        if not title or not deadline:
            flash('Title and deadline are required!', 'error')
        else:
            task = Task(title=title, deadline=deadline)
            db.session.add(task)
            db.session.commit()
            flash('Task added!', 'success')
        return redirect('/')
    tasks = Task.query.order_by(Task.id.desc()).all()
    today = date.today().isoformat()
    return render_template('index.html', tasks=tasks, today=today)

# Mark task as completed
@app.route('/done/<int:task_id>')
def done(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    flash('Task marked as completed!', 'success')
    return redirect('/')

# Edit task route
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        deadline = request.form.get('deadline', '').strip()
        if not title or not deadline:
            flash('Title and deadline are required!', 'error')
        else:
            task.title = title
            task.deadline = deadline
            db.session.commit()
            flash('Task updated!', 'success')
            return redirect('/')
    return render_template('edit.html', task=task)




if __name__ == "__main__":
    app.run(debug=True)