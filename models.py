from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users-table'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False, default="I love cooking.")
    create_date = db.Column(db.DateTime, nullable=False)
    avatar = db.Column(db.String(255), nullable=False, default="https://via.placeholder.com/200/09f/fff.png")
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class RecipeIngredientAssociation(db.Model):
    __tablename__ = "recipe-ingredient-association"
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes-table.recipe_id"), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients-table.ingredient_id"), primary_key=True)
    ingredient_quantity = db.Column(db.Numeric, nullable=False)

    ingredient = db.relationship("Ingredient", back_populates="recipes")
    recipe = db.relationship("Recipe", back_populates="ingredients")


class Recipe(db.Model):
    __tablename__ = "recipes-table"
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String(120), nullable=False)
    recipe_author = db.Column(db.String(120), nullable=False)
    recipe_date = db.Column(db.Numeric, nullable=False)
    recipe_description = db.Column(db.String(120), nullable=False)
    recipe_rating = db.Column(db.Numeric, nullable=False)
    recipe_picture = db.Column(db.String(120), nullable=False)
    recipe_cooking_time = db.Column(db.Integer, nullable=False)
    recipe_calorie_count = db.Column(db.Integer, nullable=False)

    ingredients = db.relationship("RecipeIngredientAssociation", back_populates="recipe")


class Ingredient(db.Model):
    __tablename__ = "ingredients-table"
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(120), nullable=False)
    ingredient_description = db.Column(db.String(120), nullable=False)
    ingredient_picture = db.Column(db.String(120), nullable=False)
    ingredient_calorie_count = db.Column(db.Integer, nullable=False)

    recipes = db.relationship("RecipeIngredientAssociation", back_populates="ingredient")
