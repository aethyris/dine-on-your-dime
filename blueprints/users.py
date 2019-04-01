from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from models import User, db, Filter, Recipe, Ingredient
from datetime import datetime

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


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home_page.index'))
    register = request.form
    if request.method == "POST":
        username = register.get('username')
        email = register.get('email')
        if User.query.filter_by(username=username).first() is not None:
            return render_template('signup.html', usererror=True, emailerror=False)
        elif User.query.filter_by(email=email).first() is not None:
            return render_template('signup.html', usererror=False, emailerror=True)
        else:
            user = User(username=username, email=email, create_date=datetime.utcnow())
            user.set_password(register.get('password'))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home_page.index'))
    return render_template('signup.html', usererror=False, emailerror=False)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home_page.index'))


@users.route('/user/<username>')
def view_user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)


@users.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == "POST":
        current_user.email = request.form.get('new_email')
        current_user.description = request.form.get('new_description')
        current_user.avatar = request.form.get('new_avatar_url')
        db.session.commit()
        return redirect(url_for('users.settings'))
    return render_template('settings.html', user_info=current_user)


@users.route('/settings/filter', methods=['GET', 'POST'])
@login_required
def user_filter():
    if request.method == "POST":
        info = request.form
        print(request.form.get('price_min'))
        new_filter = Filter(
            price_min=info.get('price_min'),
            price_max=info.get('price_max'),
            calorie_min=info.get('calorie_min'),
            calorie_max=info.get('calorie_max'),
            meal_type=info.get('meal_type'),
            meal_style=info.get('meal_style'),
            dietary_preferences=info.get('dietary_preferences'),
            cooking_time_min=info.get('cooking_time_min'),
            cooking_time_max=info.get('cooking_time_max')
        )
        current_user.filters = new_filter
        db.session.commit()
        return redirect(url_for('users.settings'))

    return render_template('settings.html', user_info=current_user)


@users.route('/create_recipe', methods=["GET", "POST"])
def addRecipe():
    if request.form:
        recipe = Recipe(recipe_title=request.form.get("recipe_title")), \
                 Recipe(recipe_description=request.form.get("recipe_description")), \
                 Recipe(recipe_picture=request.form.get("recipe_upload")), \
                 Recipe(recipe_cooking_time=request.form.get("recipe_cooking_time")),\
                 Recipe(recipe_calorie_count=request.form.get("recipe_calories"))
        db.session.add(recipe)
        db.session.commit()

        return render_template(settings.html, user_info=current_user)
