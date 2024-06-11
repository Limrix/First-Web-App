from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/my_name")
def my_name():
    my_name = "Matthew"
    return f"<h1>Hi my name is {my_name}</h1>"

if __name__ == "__main__":
    app.run(debug = True, port = 5000)