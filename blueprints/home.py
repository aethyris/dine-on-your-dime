from flask import Blueprint, render_template, request
from models import *
from flask_login import current_user

home_page = Blueprint('home_page', __name__, template_folder="templates")


@home_page.route('/', methods=["GET", "POST"])
def index():
    recipe_title = request.form.get("recipe_title")
    recipe_picture = request.form.get("recipe_picture")
    # print(request.form.get("recipe_title"))

    return render_template('index.html', recipe_title=recipe_title, recipe_picture=recipe_picture)

# Might Remove
@home_page.route('/recipe/<recipe_id>/admin', methods=["GET", "POST"])
def editors_choice(recipe_id=Recipe.recipe_id):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    return render_template('editorschoice.html', recipe=recipe)


@home_page.route('/editorschoice.html', methods=["GET", "POST"])
def editors_choice_iframe(recipe_id=Recipe.recipe_id):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    return render_template('editorschoice.html', recipe=recipe)


@home_page.route('/front/recipe/<recipe_id>', methods=["GET", "POST"])
def frontpage(recipe_id=Recipe.recipe_id):
    recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
    return render_template('frontpage.html', recipe=recipe)

# Might Remove


@home_page.route('/search', methods=["POST"])
def search():
    # get search results from mysql
    keyword = request.form.get("keyword")
    recipes = Recipe.query.filter((Recipe.recipe_title.contains(keyword) | Recipe.recipe_description.contains(keyword)))
    return render_template('search.html', keyword=keyword, recipes=recipes)


@home_page.route('/search2', methods=["POST"])
def filter():
    keyword = ""
    type = request.form.get("Type")
    dietary = request.form.get("Dietary")
    style = request.form.get("Style")

    if type == 'All':
        type = '*'
    if dietary == 'All':
        dietary = '*'
    # if dietary == 'All':
    #     recipes = Recipe.query.filter(
    #         (Recipe.recipe_title.contains(keyword) | Recipe.recipe_description.contains(keyword)) & (
    #             Recipe.type.equals(type)) & (Recipe.dietary_category.equals(dietary)))
    else:
        recipes = Recipe.query.filter(
            (Recipe.recipe_title.contains(keyword) | Recipe.recipe_description.contains(keyword)) & (
                Recipe.type.equals(type)) & (Recipe.dietary_category.equals(dietary)) & (
                    Recipe.recipe_title.contains(style) | Recipe.recipe_description.contains(style)))

    return render_template('search.html', keyword=keyword, recipes=recipes)
