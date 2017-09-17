from flask import Flask
from flask import request, url_for, redirect, session, render_template
app = Flask("firstFormApplication")
app.secret_key = "very_important_secret"


@app.route("/")
def generate_form():
    tasks = []
    if "tasks" in session:
        tasks = session["tasks"].split(":")
    return render_template("form.html", tasks=tasks)


@app.route("/form_handler", methods=["POST"])
def form_handler():
    task_text = request.form["task_text"]
    if "tasks" not in session:
        session["tasks"] = task_text
    else:
        session["tasks"] = task_text+":"+session['tasks']
    return redirect(url_for("generate_form"))

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
