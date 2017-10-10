from flask import Flask, render_template, request, redirect
app = Flask("helloworldApplication")

@app.route("/")
def generate_form():
    return render_template("template_q5b.html")

@app.route("/form_handler", methods=["POST"])
def process_form():
    some_text = request.form["field"]
    return "texte: "some_text

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
