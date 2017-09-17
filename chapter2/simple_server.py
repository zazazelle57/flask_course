from flask import Flask
from flask import request, url_for, make_response, redirect
app = Flask("firstFormApplication")


@app.route("/")
def generate_form():
    html_code = """<form action="%s" method="post">
        <input name="task_text" type="text" placeholder="enter what you want to do"/>
        <input type="submit"/>
    </form>""" % (url_for("form_handler"))
    return html_code


@app.route("/form_handler", methods=["POST"])
def form_handler():
    task_text = request.form["task_text"]
    return "You entered \"%s\"" % task_text


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
