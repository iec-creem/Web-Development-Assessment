from flask import Blueprint, render_template


# Set blueprint
views = Blueprint("views", __name__)


# Default/home route
@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")