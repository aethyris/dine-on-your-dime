from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import current_user, login_user
from models import User, db

users = Blueprint('users', __name__, template_folder="templates")

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page.index'))
    info = request.form
    if request.method == "POST":
        user = User.query.filter_by(username=info.get("username")).first()
        if user is not None and user.check_password(info.get("password")):
            login_user(user, remember=info.get("rememberme"))
            return redirect(url_for('home_page.index'))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)

@users.route('/signup', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home_page.index'))
    register = request.form
    if request.method == "POST":
        user = User(username=register.get('username'), email=register.get('email'))
        user.set_password(register.get('password'))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home_page.index'))
    return render_template('signup.html', error=False)