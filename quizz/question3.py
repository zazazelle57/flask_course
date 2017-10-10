from flask import Flask, render_template, request
app = Flask("helloworldApplication")

@app.route("/reponse1/<x>/<y>/<z>")
def reponse1(x, y, z):
    return y + x + z

@app.route("/reponse2/<z>/<y>/<x>")
def reponse2(x, y, z):
    return x + y + z

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
