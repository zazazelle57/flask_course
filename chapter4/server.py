from flask import Flask
from flask import request, url_for, redirect, session, render_template
app = Flask("firstFormApplication")
app.secret_key = "very_important_secret"


@app.route("/")
@app.route("/<task_list_name>")
def generate_form(task_list_name=None):
    from database import Task, TaskList
    # If no "task_list_name" parameter is provided, redirect to "default"
    if task_list_name is None:
        return redirect(url_for("generate_form", task_list_name="default"))
    existing_task_list = TaskList.query.filter_by(name=task_list_name).first()
    # If no existing task list, then create a new one
    if existing_task_list is None:
        new_task_list = TaskList()
        new_task_list.name = task_list_name
        db.session.add(new_task_list)
        db.session.commit()
        existing_task_list = new_task_list
    # Render the form usign the current task list
    return render_template("form.html", task_list=existing_task_list)


@app.route("/form_handler", methods=["POST"])
def form_handler():
    from database import Task
    task_list_id = request.form["task_list_id"]
    task_list_name = request.form["task_list_name"]
    task_text = request.form["task_text"]

    # Create a new task
    new_task = Task()
    new_task.label = task_text
    new_task.isDone = False
    new_task.task_list_id = task_list_id # Make the link between Task and TaskList

    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for("generate_form", task_list_name=task_list_name))

if __name__ == "__main__":
    # Create the DB
    from database import db
    print("creating database")
    db.create_all()
    print("database created")
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
