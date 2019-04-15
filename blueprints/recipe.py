from flask import Blueprint, render_template
from models import User, db, Filter, Recipe, Ingredient


recipes = Blueprint('recipes', __name__, template_folder="templates")


@recipes.route('/recipe/<recipe_id>')
def show_recipe(recipe_id, username=User.username):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    user = User.query.filter_by(username=username).first()
    return render_template('recipe.html', recipe=recipe, user=user)


# @recipes.route('/recipe/<recipe_id>/admin')
# def promote_recipe(recipe_id, username=User.username):
#     recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
#     user = User.query.filter_by(username=username).first()
#     return render_template('frontpage.html', recipe=recipe, user=user)


# @recipes.route('/recipe/<recipe_id>/admin')
# def promote_recipe(recipe_id, username=User.username):
#     recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
#     user = User.query.filter_by(username=username).first()
#     return render_template('index.html', recipe=recipe, user=user)


# @recipes.route('/index/recipe/<recipe_id>')
# def return_to_index(recipe_id):
#     recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
#     return render_template('index.html', recipe=recipe)
