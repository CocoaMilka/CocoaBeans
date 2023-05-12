from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('user_name')
        password = request.form.get('user_pass')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            
            else:
                flash('Incorrect password!', category='error')

        else:
            flash('User does not exist.', category='error')


    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('user_name')
        password1 = request.form.get('user_pass')
        password2 = request.form.get('user_pass2')

        # ensure data is valid
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username taken!', category='error')
        elif len(username) < 1:
            flash('Username cannot be NULL.', category='error')
        elif password1 != password2:
            flash('Passwords not matching.', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()

            flash('Account created!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("sign-up.html")