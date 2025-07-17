from flask import Blueprint, render_template


# Set blueprint
views = Blueprint("views", __name__)


# Default/home route
@views.route("/")
@views.route("/home")
@views.route("/index")
def home():
    return render_template("home.html")

# game1 route
@views.route("/game1")
def game1():
    return render_template("game1.html")