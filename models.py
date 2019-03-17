from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Recipe(db.Model):
    __tablename__ = "recipes"
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String, nullable=False)
    recipe_author = db.Column(db.String, nullable=False)
    recipe_date = db.Column(db.String, nullable=False)
    recipe_rating = db.Column(db.Decimal, nullable=False)
    recipe_picture = db.Column(db.String, nullable=False)
    recipe_cooking_time = db.Column(db.Integer, nullable=False)
    recipe_calorie_count = db.Column(db.Integer, nullable=False)

    ri_recipe = db.Column(db.Integer, db.ForeignKey("recipe_ingredient"), nullable=False)


class Ingredient(db.Model):
    __tablename__ = "ingredients"
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String, nullable=False)
    ingredient_description = db.Column(db.String, nullable=False)
    ingredient_picture = db.Column(db.String, nullable=False)
    ingredient_calorie_count = db.Column(db.Integer, nullable=False)

    ri_ingredient = db.Column(db.Integer, db.ForeignKey("recipe_ingredient"), nullable=False)


class Recipe_Ingredient(db.Model):
    __tablename__ = "recipe_ingredients"
    ri_id = db.Column(db.Integer, primary_key=True)
    ri_recipe_id = db.Column(db.Integer, nullable=False)
    ri_ingredient_id = db.Column(db.Integer, nullable=False)
    ri_ingredient_quantity = db.Column(db.Integer, nullable=False)
