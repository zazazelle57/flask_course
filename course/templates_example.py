from flask import Flask, render_template, request
app = Flask("helloworldApplication")


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

    # return render_template("tasks_template.html",
    #                        title=title,
    #                        tasks_list=tasks)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
