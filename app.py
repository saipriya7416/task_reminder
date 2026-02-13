from flask import Flask, render_template, request, redirect
from datetime import date
app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        task_date = request.form["date"]
        tasks.append([title, task_date, 0])
        return redirect("/")
    today = date.today().isoformat()
    return render_template("index.html", tasks=tasks, today=today)


@app.route("/done/<int:id>")
def done(id):
    tasks[id][2] = 1
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)