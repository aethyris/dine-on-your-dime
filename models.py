from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Recipe(db.Model):
    __tablename__ = "recipes"
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String, nullable=False)
    recipe_author = db.Column(db.String, nullable=False)
    recipe_date = db.Column(db.String, nullable=False)
    recipe_contents = db.Column(db.String, nullable=False)
    recipe_rating = db.Column(db.String, nullable=False)
    recipe_picture = db.Column(db.String, nullable=False)

