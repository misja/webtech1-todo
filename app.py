from forms import TaskForm
from models import db, Task
from filters import type_to_name, time_from_now
from flask import Flask, render_template, redirect, flash, url_for, request

app = Flask(__name__)

app.config["SECRET_KEY"] = "xsfd567sha905ea54p0"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.jinja_env.filters["type_to_name"] = type_to_name
app.jinja_env.filters["time_from_now"] = time_from_now

db.init_app(app)


@app.route("/")
def home():
    """Landing page

    Acts as a landing page and as a tasks listing page
    """
    tasks = db.session.execute(db.select(Task).order_by(Task.deadline.desc())).scalars()

    return render_template("index.html", tasks=tasks)


@app.route("/tasks", methods=["GET", "POST"])
def create_task():
    """Create a task"""
    form = TaskForm()

    if request.method == "POST":
        if form.validate_on_submit():
            task = Task()
            form.populate_obj(task)

            db.session.add(task)
            db.session.commit()

            flash("Task created", "success")

            return redirect(url_for("home"))
        else:
            flash("Could not create task", "warning")

    return render_template("tasks/create.html", form=form)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def read_task(task_id):
    """Read a task"""
    task = db.get_or_404(Task, task_id)
    return render_template("tasks/detail.html", task=task)


@app.route("/tasks/<int:task_id>/update", methods=["GET", "POST"])
def update_task(task_id):
    """Update a task"""
    task = db.get_or_404(Task, task_id)
    form = TaskForm(obj=task)

    if request.method == "POST":
        if form.validate_on_submit():
            form.populate_obj(task)

            db.session.add(task)
            db.session.commit()

            flash("Task updated", "success")

            return redirect(url_for("read_task", task_id=task_id))
        else:
            flash("Could not update task", "warning")

    return render_template("tasks/update.html", form=form)


@app.route("/tasks/<int:task_id>/delete", methods=["GET"])
def delete_task(task_id):
    """Delete a task"""
    task = db.get_or_404(Task, task_id)

    db.session.delete(task)
    db.session.commit()

    flash("Task deleted", "success")

    return redirect(url_for("home"))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
