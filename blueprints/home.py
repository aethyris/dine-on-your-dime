from flask import Blueprint, render_template, request

home_page = Blueprint('home_page', __name__, template_folder="templates")


@home_page.route('/')
def index():
    return render_template('index.html')


@home_page.route('/search', methods=["POST"])
def search():
    # get search results from mysql
    keyword = request.form.get("keyword")
    return render_template('search.html', keyword=keyword)


# @home_page.route('/search/recipe')
# def recipe():
#     # show recipe from search results
#     return render_template('recipe.html')
