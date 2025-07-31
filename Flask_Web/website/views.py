from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Note
from . import db

# Set blueprint
views = Blueprint("views", __name__)


# Default/home route
@views.route("/")
@views.route("/home")
@views.route("/index")
def home():
    return render_template("home.html", user=current_user)

# game1 route
@views.route("/game1")
def game1():
    return render_template("game1.html", user=current_user)

# contact route
@views.route("/contact", methods=['POST', 'GET'])
@login_required
def contact():
    if request.method == 'POST':
        note = request.form.get('note') # Gets the note from the HTML
        if len(note) < 1:
            flash('Comment field cannot be empty')
        else:
            new_note = Note(data=note, user_id=current_user.id) # Providing the schema for the note
            db.session.add(new_note) # adding the note to the database
            db.session.commit()
            flash('Comment added!', category='success')
    return render_template("contact.html", user=current_user)