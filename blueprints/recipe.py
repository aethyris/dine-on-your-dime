from flask import Blueprint, render_template
from models import User, db, Filter, Recipe, Ingredient


recipes = Blueprint('recipes', __name__, template_folder="templates")


@recipes.route('/recipe/<recipe_id>')
def show_recipe(recipe_id):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    return render_template('recipe.html', recipe=recipe)
