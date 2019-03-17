from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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

