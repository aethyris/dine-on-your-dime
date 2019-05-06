from flask import Blueprint, render_template, redirect, url_for
from models import User, db, Recipe, Ingredient
from flask_login import login_required, current_user

recipes = Blueprint('recipes', __name__, template_folder="templates")


@recipes.route('/recipe/<recipe_id>')
def show_recipe(recipe_id):
    """
    This function handles the logic for displaying recipe information in the recipe.html page
    :param recipe_id: Every recipe contains a unique ID
    :param username: Every recipe is tied to a User
    :param ingredient_name: (No use currently)
    :return: recipe.html
    """
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    return render_template('recipe.html', recipe=recipe, user=current_user)

@recipes.route('/recipe/<recipe_id>/like')
@login_required
def like_recipe(recipe_id):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first_or_404()
    recipe.user_liked.append(current_user)
    db.session.commit()
    return redirect(url_for('recipes.show_recipe', recipe_id=recipe_id))

@recipes.route('/recipe/<recipe_id>/unlike')
@login_required
def unlike_recipe(recipe_id):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first_or_404()
    recipe.user_liked.remove(current_user)
    db.session.commit()
    return redirect(url_for('recipes.show_recipe', recipe_id=recipe_id))

@recipes.route('/recipe/<recipe_id>/favorite')
@login_required
def favorite_recipe(recipe_id):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first_or_404()
    recipe.user_favorites.append(current_user)
    db.session.commit()
    return redirect(url_for('recipes.show_recipe', recipe_id=recipe_id))

@recipes.route('/recipe/<recipe_id>/unfavorite')
@login_required
def unfavorite_recipe(recipe_id):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first_or_404()
    recipe.user_favorites.remove(current_user)
    db.session.commit()
    return redirect(url_for('recipes.show_recipe', recipe_id=recipe_id))