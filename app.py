import os
import sys, traceback
from flask import Flask, render_template, session, request
from flask_login import LoginManager
import sys
from flask import Flask, render_template
from flask_login import LoginManager, current_user
from flask_bootstrap import Bootstrap
from blueprints.home import home_page
from blueprints.users import users
from blueprints.recipe import recipes
from blueprints.errors import errors
from blueprints.calendar import calendar
from blueprints.leaderboard import leaderboard
from config import Config
from models import db, User
from sockets import socketio
from forms import FilterForm

app = Flask(__name__)
login = LoginManager(app)
socketio.init_app(app)
app.config.from_object(Config)
db.init_app(app)
Bootstrap(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Login User Loader

@login.user_loader
def load_user(id):  # setting users to sessions
    return User.query.get(int(id))


# Blueprints

app.register_blueprint(home_page)
app.register_blueprint(users)
app.register_blueprint(recipes)
app.register_blueprint(errors)
app.register_blueprint(calendar)
app.register_blueprint(leaderboard)


# 404 Handler

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.context_processor
def inject_filter():
    """
    Ensures that the there is a filterform on each page.
    """
    if current_user.is_authenticated:
        return dict(search_filter=FilterForm(obj=current_user.filters))
    else:
        return dict(search_filter=FilterForm())


def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'createdb':
            db.create_all()
            print("Created database.")
        elif sys.argv[1] == 'deltables':
            db.reflect()
            db.drop_all()
            db.session.commit()
    app.run(host='0.0.0.0', port='8080')


if __name__ == "__main__":
    with app.app_context():
        main()


@app.route("/upload", methods = ["POST"])
def upload():
    photo = os.path.join(APP_ROOT, "images/")
    print(photo)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([photo, filename])
        print(destination)
        file.save(destination)
    return render_template("recipe.html")

@app.route("/comment", methods = ["POST"])
def comment():
    recipe = "recipes-table"
    for recipe in recipe.comments:
        print(get_comments)

@app.route("/popular")
def most_popular():
    if (Recipe.recipe_rating > 0):
        Recipe.recipe_rating.sort(reverse=True)
        popularList = sorted(Recipe.recipe_rating, reverse=True)

        print(popularList[0])
        print(popularList[1])
        print(popularList[2])
    return render_template("layout.html")
