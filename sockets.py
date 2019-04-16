from flask_socketio import SocketIO, emit
from flask import request, session
from flask_login import current_user

socketio = SocketIO()
user_sid_dict = {}

@socketio.on('connect')
def on_connect():
    user_sid_dict[current_user.id] = request.sid

@socketio.on('disconnect')
def on_disconnect():
    user_sid_dict.pop(current_user.id)

def emit_new_recipe(recipe, id):
    room = user_sid_dict.get(id)
    if room is not None:
        print('emit new recipe')
        socketio.emit('new recipe', recipe, namespace='/userfeed', room=room)

@socketio.on('load', namespace='/userfeed')
def load_recipes(user_id, page):
    recipes = current_user.followed_recipes()
    room = user_sid_dict.get(user_id)
    json_data = [{'total': recipes.count()},]
    for recipe in recipes.paginate(page, 10, False).items:
        dict_data = {
            'id': recipe.recipe_id,
            'title': recipe.recipe_title,
            'date': str(recipe.recipe_date),
            'author': recipe.recipe_author.username,
            'picture': recipe.recipe_picture,
            'rating': str(recipe.recipe_rating),
            'cooking_time': recipe.recipe_cooking_time,
            'calorie_count': recipe.recipe_calorie_count
        }
        json_data.append(dict_data)
    socketio.emit('render', json_data, namespace='/userfeed', room=room)