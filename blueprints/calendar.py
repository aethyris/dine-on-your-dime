from flask import Blueprint, request, render_template, redirect, url_for, Response
from models import User, db, Recipe, PlannedRecipeAssociation
from flask_login import current_user, login_required
from datetime import datetime, timedelta
import json

calendar = Blueprint('calendar', __name__, template_folder="templates")


@calendar.route('/user/<username>/calendar')
def view_calendar(username):
    """
    Main page to view a user's meal plan.
    """
    return render_template('calendar.html', username=username)


@calendar.route('/user/<username>/calendar/data')
def return_data(username):
    """
    Returns a JSON list of planned recipes to FullCalendar.
    """
    user_id = User.query.filter_by(username=username).first().id
    recipes = PlannedRecipeAssociation.query.filter_by(user_id=user_id).all()
    json_data = []
    for planned_recipe in recipes:
        dict_data = {
            'assoc': planned_recipe.id,
            'title': planned_recipe.recipe.recipe_title,
            'start': planned_recipe.start,
            'end': planned_recipe.end,
            'description': planned_recipe.recipe.recipe_description,
            'notes': planned_recipe.notes,
            'recipe_url': url_for('home_page.index')
        }
        json_data.append(dict_data)
    return Response(json.dumps(json_data), mimetype='application/json')


@calendar.route('/user/calendar/add', methods=['POST'])
@login_required
def add_data():
    """
    Adds a recipe to a user's meal plan.

    Adds a PlannedRecipeAssociation model to the MySQL databsae based off of the form information.
    In current implementation, the Ajax Form Plugin prevents us from reaching the redirect.
    """
    if request.method == 'POST':
        recipe = Recipe.query.filter_by(recipe_id=request.form.get('recipe')).first()
        start_time = str(request.form.get('dt'))
        duration = int(recipe.recipe_cooking_time)
        end_time = (datetime.fromisoformat(start_time) + timedelta(minutes=duration)).isoformat()
        notes = request.form.get('notes')
        assoc = PlannedRecipeAssociation(user=current_user, recipe=recipe, start=start_time, end=end_time, notes=notes)
        db.session.add(assoc)
        db.session.commit()
    return redirect(url_for('calendar.view_calendar', username=current_user.username))


@calendar.route('/user/calendar/remove/', methods=['POST'])
@login_required
def remove_data():
    """
    Removes a planned recipe from the meal plan.

    This removes based on the id of the association, so it can remove any user's planned recipe.
    In current implementation, the Ajax Form Plugin prevents us from reaching the redirect.
    """
    if request.method == 'POST':
        assoc = PlannedRecipeAssociation.query.filter_by(id=request.form.get('assoc_id')).first()
        db.session.delete(assoc)
        db.session.commit()
    return redirect(url_for('calendar.view_calendar', username=current_user.username))


@calendar.route('/user/calendar/edit', methods=['POST'])
@login_required
def edit_data():
    """
    Edits a planned recipe.

    This can edit any planned recipe since it use's the association id.
    In current implementation, the Ajax Form Plugin prevents us from reaching the redirect.
    """
    if request.method == 'POST':
        assoc = PlannedRecipeAssociation.query.filter_by(id=request.form.get('assoc_id')).first()
        start_time = str(request.form.get('edit_start'))
        assoc.start = start_time
        assoc.end = (datetime.fromisoformat(start_time) + timedelta(
            minutes=assoc.recipe.recipe_cooking_time)).isoformat()
        assoc.notes = request.form.get('edit_notes')
        db.session.commit()
    return redirect(url_for('calendar.view_calendar', username=current_user.username))
