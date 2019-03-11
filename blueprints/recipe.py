from flask import Blueprint, render_template

recipes = Blueprint('recipes', __name__, template_folder="templates")

@recipes.route('/recipe/<recipe_id>')
def search():
    # get search results
    return render_template('recipe.html')