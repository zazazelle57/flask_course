from flask import Flask, render_template, request
app = Flask("helloworldApplication")

@app.route("/msG/plouf")
def reponse1():
    return "msg: abcd"

@app.route("/msg/<message>")
def reponse2(message):
    return "msg: "+message

@app.route("/msg/<message>/<plouf>")
def reponse3(message, plouf):
    return "msg: "+message+"_"+plouf

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
