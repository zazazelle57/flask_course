from flask import Flask, render_template, request
app = Flask("helloworldApplication")

@app.route("/url")
def view():
    return "HelloWorld!"

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
