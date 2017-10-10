from flask import Flask, render_template, request
app = Flask("helloworldApplication")

@app.route("/get_template")
def template():
    list1 = [1,2,3,4]
    list2 = [5,6,7,8]
    return render_template("template_q4.html", l1=list2, l2=list1)

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8080, debug=True)
