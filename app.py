import sys, traceback
from flask import Flask, render_template
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from blueprints.home import home_page
from blueprints.users import users
from blueprints.recipe import recipes
from blueprints.errors import errors
from blueprints.calendar import calendar
from config import Config
from models import db, User, RecipeIngredientAssociation, Recipe, Ingredient, Filter, PlannedRecipeAssociation

app = Flask(__name__)
app.debug = True
login = LoginManager(app)
app.secret_key = 'much secret'  # for some reason flask_login needs a secret key?
app.config.from_object(Config)
db.init_app(app)
Bootstrap(app)

# Admin Settings
app.config['FLASK_ADMIN_SWATCH'] = 'sandstone'
admin = Admin(app, name='Dine on Your Dime (ADMIN)', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(RecipeIngredientAssociation, db.session))
admin.add_view(ModelView(Recipe, db.session))
admin.add_view(ModelView(Ingredient, db.session))
admin.add_view(ModelView(Filter, db.session))
admin.add_view(ModelView(PlannedRecipeAssociation, db.session))


# Admin Settings

@login.user_loader
def load_user(id):  # setting users to sessions
    return User.query.get(int(id))


app.register_blueprint(home_page)
app.register_blueprint(users)
app.register_blueprint(recipes)
app.register_blueprint(errors)
app.register_blueprint(calendar)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


def main():
    if (len(sys.argv) == 2):
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
