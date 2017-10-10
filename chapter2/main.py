from flask import Flask
from flask import request, url_for, redirect, session
app = Flask("firstFormApplication")
app.secret_key = "very_important_secret"


@app.route("/")
def generate_form():

    html_code = """<form action="%s" method="post">
        <input name="task_text" type="text" placeholder="enter what you want to do"/>
        <input type="submit"/>
    </form>""" % (url_for("form_handler"))

    if "tasks" in session:
        html_code += "<ul>"
        for task in session['tasks'].split(":"):
            html_code += "<li>%s</li>" % (task)
        html_code += "</ul>"

    return html_code


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
