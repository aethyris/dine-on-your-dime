from flask import Blueprint, request, render_template, redirect, url_for, Response
from models import User, db, Recipe, PlannedRecipeAssociation
from flask_login import current_user, login_required
from datetime import datetime
import json

calendar = Blueprint('calendar', __name__, template_folder="templates")

@calendar.route('/user/<username>/calendar')
def view_calendar(username):
    return render_template('calendar.html', username=username)

@calendar.route('/user/<username>/calendar/data')
def return_data(username):
    user_id = User.query.filter_by(username=username).first().id
    recipes = PlannedRecipeAssociation.query.filter_by(user_id=user_id).all()
    json_data = []
    for planned_recipe in recipes:
        dict_data = {'title': planned_recipe.recipe.recipe_title, 'start': planned_recipe.start, 'description': planned_recipe.recipe.recipe_description}
        json_data.append(dict_data)
    return Response(json.dumps(json_data), mimetype='application/json')

@calendar.route('/user/calendar/add', methods=['POST'])
@login_required
def add_data():
    if request.method == 'POST':
        recipe = Recipe.query.filter_by(recipe_id=request.form.get('recipe')).first()
        assoc = PlannedRecipeAssociation(user=current_user, recipe=recipe, start=datetime.now().replace(microsecond=0).isoformat())
        db.session.add(assoc)
        db.session.commit()
    return redirect(url_for('calendar.view_calendar', username=current_user.username)) 

@calendar.route('/user/calendar/remove/', methods=['POST'])
@login_required
def remove_data(recipe_id):
    if request.method == 'POST':
        assoc = PlannedRecipeAssociation.query.filter_by(recipe_id=request.form.get('recipe')).first()
        db.session.remove(assoc)
        db.session.commit()
    return redirect(url_for('calendar.view_calendar', username=current_user.username))