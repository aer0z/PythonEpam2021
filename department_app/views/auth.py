from . import page
from flask import render_template, request, flash


@page.route('/')
def home():
    return render_template("home.html")


@page.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@page.route('/logout')
def logout():
    return '<p>Logout</p>'


@page.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to database
            flash('Account created!', category='success')
    return render_template('sign_up.html')
