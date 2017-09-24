from flask import Flask, render_template, request
app = Flask("helloworldApplication")

@app.route("/")
def generate_form():
    return render_template("simple_form.html")

@app.route("/process_form", methods=["POST"])
def process_form():
    nickname = request.form["nickname"]
    age = request.form["age"]

    return render_template("hello_template.html", nickname=nickname, age=age)

@app.route("/plop")
def template_example():
    title = "A todo list"
    tasks = ["learning flask", "write a \
            template", "learn database \
            querying", "finish the project"]

    result = "<h1>"+title+"</h1>"
    result += "<ul>"
    result += "\n".join(map(lambda t: "<li>"+t+"</li>", tasks))
    result += "</ul>"

    return result

    return render_template("tasks_template.html",
                           title=title,
                           tasks_list=tasks)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)