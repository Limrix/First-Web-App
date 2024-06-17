from flask import render_template, Blueprint
from fav_bands import favourite_bands

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def about():
    return render_template("page2.html", favourite_bands = favourite_bands)

@my_view.route("/my_name")
def contact():
    my_name = "Matthew"
    return render_template("page3.html", my_name = my_name)