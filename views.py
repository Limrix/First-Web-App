from flask import render_template, Blueprint, request
from fav_bands import favourite_bands

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/page2")
def page2():
    return render_template("page2.html", favourite_bands = favourite_bands)

@my_view.route("/page3", methods=["GET", "POST"])
def page3():
    if request.method =="POST":
        new_band = request.form["added_band"]
        favourite_bands.append(new_band)

    return render_template("page3.html")