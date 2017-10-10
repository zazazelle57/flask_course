from flask import Flask, url_for
app = Flask("helloworldApplication")


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello/<firstname>/<lastname>/<int:age>")
def hello_name_age(firstname, lastname, age):
    return "Hello %s %s, you are %i years old" % (firstname, lastname, age)


@app.route("/fail_divide_zero")
def fail_divide_zero():
    i = 10
    j = 0
    return "%i" % (i / j)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)