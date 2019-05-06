import sys
from flask import Flask, render_template
from flask_login import LoginManager, current_user
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from blueprints.home import home_page
from blueprints.users import users
from blueprints.recipe import recipes
from blueprints.errors import errors
from blueprints.calendar import calendar
from blueprints.leaderboard import leaderboard
from config import Config
from models import db, User, RecipeIngredientAssociation, Recipe, Ingredient, Filter, PlannedRecipeAssociation
from sockets import socketio
from forms import FilterForm

app = Flask(__name__)
app.debug = True
login = LoginManager(app)
socketio.init_app(app)
app.config.from_object(Config)
db.init_app(app)
Bootstrap(app)


# Admin Settings


# app.config['FLASK_ADMIN_SWATCH'] = 'sandstone'
# admin = Admin(app, name='Dine on Your Dime (ADMIN)', template_mode='bootstrap3')
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(RecipeIngredientAssociation, db.session))
# admin.add_view(ModelView(Recipe, db.session))
# admin.add_view(ModelView(Ingredient, db.session))
# admin.add_view(ModelView(Filter, db.session))
# admin.add_view(ModelView(PlannedRecipeAssociation, db.session))


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


if __name__ == "__main__":
    with app.app_context():
        main()


def most_popular(db):
    if (recipe_rating > 0):
        recipe_rating.sort(reverse=True)
        popularList = sorted(recipe_rating, reverse=True)
        print(popularList[0])
        print(popularList[1])
