from flask import Blueprint, render_template, request
from flask_login import login_required
from models import *

home_page = Blueprint('home_page', __name__, template_folder="templates")


@home_page.route('/')
def index():
    return render_template('index.html')

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
