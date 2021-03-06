"""
Module for logic of login and registration
"""

from . import page
from flask import render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from department_app.service import auth_service
from flask_login import login_user, logout_user, login_required, current_user


@page.route('/')
@login_required
def home():
    """
    Render main page
    :return: main page
    """
    return render_template("home.html", user=current_user)


@page.route('/login', methods=['GET', 'POST'])
def login():
    """
    Render login page
    :return: login page
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = auth_service.email_exists(email=email)
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('page.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template('login.html', user=current_user)


@page.route('/logout')
@login_required
def logout():
    """
    Logout user
    :return: redirect to main page
    """
    logout_user()
    return redirect(url_for('page.login'))


@page.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    Render registration page
    :return: registration page
    """
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = auth_service.email_exists(email=email)
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 6:
            flash('Password must be at least 7 characters.', category='error')
        else:
            psw = generate_password_hash(password1, method='sha256')
            auth_service.new_user(email, psw, first_name)
            flash('Account created!', category='success')
            return redirect(url_for('page.login'))
    return render_template('sign_up.html', user=current_user)
