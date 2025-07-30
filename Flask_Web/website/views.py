from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user


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

# contact route
@views.route("/contact")
@login_required
def contact():
    return render_template("contact.html")