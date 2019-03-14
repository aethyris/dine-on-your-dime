from flask import Blueprint, render_template, request
from models import *

home_page = Blueprint('home_page', __name__, template_folder="templates")

@home_page.route('/')
def index():
    return render_template('index.html')

@home_page.route('/search', methods=["POST"])
def search():
    keyword = request.form.get("keyword")
    recipes = Recipe.query.filter((Recipe.recipe_title.contains(keyword) | Recipe.recipe_description.contains(keyword)))
    return render_template('search.html', keyword=keyword, recipes=recipes)