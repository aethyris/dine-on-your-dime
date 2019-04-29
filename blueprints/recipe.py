from flask import Blueprint, render_template
from models import User, Recipe, Ingredient

recipes = Blueprint('recipes', __name__, template_folder="templates")


@recipes.route('/recipe/<recipe_id>')
def show_recipe(recipe_id, username=User.username, ingredient_name=Ingredient.ingredient_name):
    """
    This function handles the logic for displaying recipe information in the recipe.html page
    :param recipe_id: Every recipe contains a unique ID
    :param username: Every recipe is tied to a User
    :param ingredient_name: (No use currently)
    :return: recipe.html
    """
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    user = User.query.filter_by(username=username).first()
    ingredient = Ingredient.query.filter_by(ingredient_name=ingredient_name)
    return render_template('recipe.html', recipe=recipe, user=user, ingredient=ingredient)
