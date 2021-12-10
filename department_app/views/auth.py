
from . import page
from flask import render_template


@page.route('/')
def home():
    return render_template("home.html")


@page.route('/login')
def login():
    return render_template('login.html')


@page.route('/logout')
def logout():
    return '<p>Logout</p>'


@page.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')
