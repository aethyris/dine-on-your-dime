from flask import Blueprint, render_template, redirect, url_for, request, abort, Response
from flask_login import current_user, login_user, logout_user, login_required
from models import User, db, Filter, Recipe, Ingredient
from forms import LoginForm, RegistrationForm, UserInfoForm, FilterForm
from datetime import datetime
from sockets import emit_new_recipe
import threading

users = Blueprint('users', __name__, template_folder="templates")


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return render_template('login.html', form=form)
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home_page.index'))
    return render_template('login.html', form=form)


@users.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home_page.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.filters = Filter()
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('signup.html', form=form)


@users.route('/logout')
@login_required
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
    info_form = UserInfoForm(obj=current_user)
    filter_form = FilterForm(obj=current_user.filters)
    # Modifying User Info
    # if info_form.validate_on_submit():
    #     current_user.username = info_form.username.data
    #     current_user.description = info_form.description.data
    #     current_user.avatar = info_form.avatar.data
    #     current_user.email = info_form.email.data
    #     db.session.commit()
    #     return redirect(url_for('users.settings'))
    # Modifying User Filter
    if filter_form.validate_on_submit():
        current_user.filters.price_min = filter_form.price_min.data
        current_user.filters.price_max = filter_form.price_max.data
        current_user.filters.calorie_min = filter_form.calorie_min.data
        current_user.filters.calorie_max = filter_form.calorie_max.data
        current_user.filters.meal_type = filter_form.meal_type.data
        current_user.filters.meal_style = filter_form.meal_style.data
        current_user.filters.dietary_preferences = filter_form.dietary_preferences.data
        current_user.filters.cooking_time_min = filter_form.cooking_time_min.data
        current_user.filters.cooking_time_max = filter_form.cooking_time_max.data
        db.session.commit()
        return redirect(url_for('users.settings'))
    return render_template('settings.html', user_info=current_user, info_form=info_form, filter_form=filter_form)


def handle_new_recipe(recipe, follower_ids):
    """
    Helper method used to send SocketIO event to the rooms of the followers.
    """
    data = {
        'id': recipe.recipe_id,
        'title': recipe.recipe_title,
        'date': str(recipe.recipe_date),
        'author': recipe.recipe_author.username,
        'picture': recipe.recipe_picture,
        'rating': str(recipe.recipe_rating),
        'cooking_time': recipe.recipe_cooking_time,
        'calorie_count': recipe.recipe_calorie_count
    }
    for i in follower_ids:
        emit_new_recipe(data, i)


@users.route('/create_recipe', methods=["GET", "POST"])
@login_required
def add_recipe():
    """
    After user enters recipe information into forms in settings.html this
    function adds the recipe to the database
    :return: index.html
    """
    if request.method == "POST":
        user_recipe = Recipe(
            recipe_title=request.form.get("recipe_title"),
            recipe_date=datetime.utcnow(),
            recipe_description=request.form.get("recipe_description"),
            recipe_rating=5,
            recipe_picture=request.form.get("recipe_picture"),
            recipe_cooking_time=request.form.get("recipe_cooking_time"),
            recipe_calorie_count=request.form.get("recipe_calorie_count")
        )
        current_user.recipes.append(user_recipe)
        db.session.add(user_recipe)

        # threading for sending socketIO event
        follower_ids = [follower.id for follower in user_recipe.recipe_author.followers]
        thr = threading.Thread(target=handle_new_recipe, args=(user_recipe, follower_ids))
        thr.daemon = True
        thr.start()

        db.session.commit()

    def add_ingredient():
        if request.method == 'POST':
            recipe_ingredient = Ingredient(
                ingredient_name=request.form.get("recipe_ingredient"))

            db.session.add(recipe_ingredient)
            db.session.commit()
    return render_template('index.html')


@users.route('/feed/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first_or_404()
    if user == current_user:
        return redirect(url_for('users.view_user', username=username))
    current_user.follow(user)
    db.session.commit()
    return redirect(url_for('users.view_user', username=username))


@users.route('/feed/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first_or_404()
    if user == current_user:
        return redirect(url_for('users.view_user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    return redirect(url_for('users.view_user', username=username))

@users.route('/like/<int:post_id>/<action>')
@login_required
def like_action(post_id, action):
        post = Post.query.filter_by(id=post_id).first_or_404()
        if action == 'like':
            current_user.like_post(post)
            db.session.commit()
        if action == 'unlike':
            current_user.unlike_post(post)
            db.session.commit()
        return render_template('leaderboard.html')

@users.route('/feed')
@login_required
def feed():
    return render_template('feed.html')