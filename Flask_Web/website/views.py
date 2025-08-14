from flask import Blueprint, render_template, url_for, request, flash, redirect, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Note
import json
from . import db

# Set blueprint
views = Blueprint("views", __name__)


# Default/home route
@views.route("/")
@views.route("/home")
@views.route("/index")
def home():
    return render_template("home.html", user=current_user)

# Undertale route
@views.route("/undertale")
def undertale():
    return render_template("game1.html", user=current_user)

# Pokemon route
@views.route("/pokemon")
def pokemon():
    return render_template("game2.html", user=current_user)

# Hollow Knight route
@views.route("/hollow-knight")
def hollow_knight():
    return render_template("game3.html", user=current_user)

# contact route
@views.route("/contact", methods=['POST', 'GET'])
@login_required
def contact():
    if request.method == 'POST':
        note = request.form.get('note') # Gets the note from the HTML
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id) # Providing the schema for the note
            db.session.add(new_note) # adding the note to the database
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("contact.html", user=current_user)

# Delete note route
@views.route("/delete-note", methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted!', category='success')
    
    return jsonify({})