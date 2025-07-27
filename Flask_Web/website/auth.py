from flask import Blueprint, render_template, url_for, request, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Note
from . import db

auth = Blueprint('auth', __name__)


# Sign Up route
@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email is not valid.', category='error')
        elif len(username) < 2:
            flash('Username must be at least 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) <8:
            flash('Password must have at least 8 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='scrypt:32768:8:1'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!', category='success')
            
    return render_template("sign_up.html", user=current_user)
    