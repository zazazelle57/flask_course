from flask import Flask, render_template, request
app = Flask("helloworldApplication")


@app.route("/")
def generate_form():
    return render_template("simple_form.html")


@app.route("/process_form", methods=["POST"])
def process_form():
    nickname = request.form["nickname"]
    age = request.form["age"]

    return render_template("template_q4b.html", nickname=nickname, age=age)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
