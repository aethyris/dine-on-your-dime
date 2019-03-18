import sys
from flask import Flask
from flask_login import LoginManager
from blueprints.home import home_page
from blueprints.users import users
from blueprints.recipe import recipes
from config import Config
from models import db, User

app = Flask(__name__)
login = LoginManager(app)
app.secret_key = 'much secret' # for some reason flask_login needs a secret key?
app.config.from_object(Config)
db.init_app(app)

@login.user_loader
def load_user(id): # setting users to sessions
    return User.query.get(int(id))

app.register_blueprint(home_page)
app.register_blueprint(users)
app.register_blueprint(recipes)


def main():
    if (len(sys.argv)==2):
        if sys.argv[1] == 'createdb':
            db.create_all()
            print("Created database.")
        elif sys.argv[1] == 'cleardb':
            db.reflect()
            db.drop_all()

if __name__ == "__main__":
    with app.app_context():
        main()