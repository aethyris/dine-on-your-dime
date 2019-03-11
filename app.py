import sys
from flask import Flask
from blueprints.home import home_page
from config import Config
from models import *

app = Flask(__name__)
app.config.from_object(Config)
# db.init_app(app)

app.register_blueprint(home_page)

#def main():
    #if (len(sys.argv)==2):
        #if sys.argv[1] == 'createdb':
            #db.create_all()
            #print("Created database.")

#if __name__ == "__main__":
    #with app.app_context():
        #main()